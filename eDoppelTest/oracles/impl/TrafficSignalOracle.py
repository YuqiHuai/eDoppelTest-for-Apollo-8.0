import re
from typing import Dict, List, Optional, Set, Tuple

from shapely.geometry import LineString, Polygon

from apollo.map_service import MapService
from apollo.proto_v8.modules.common_msgs.localization_msgs.localization_pb2 import (
    LocalizationEstimate,
)
from apollo.proto_v8.modules.common_msgs.perception_msgs.traffic_light_detection_pb2 import (
    TrafficLight,
    TrafficLightDetection,
)
from apollo.proto_v8.modules.common_msgs.planning_msgs.decision_pb2 import (
    STOP_REASON_SIGNAL,
)
from apollo.proto_v8.modules.common_msgs.planning_msgs.planning_pb2 import ADCTrajectory
from apollo.utils import calculate_velocity, generate_adc_polygon
from config import HD_MAP
from eDoppelTest.oracles.OracleInterface import OracleInterface
from utils import get_map_service_for_map


class TrafficSignalOracle(OracleInterface):
    """
    The Traffic Signal Oracle is responsible for checking if the ADS instance violates a red light
    signal. When the AV is facing a red light signal and the AV is already intersecting the stop line,
    it should not have positive speed because it should have stopped before the stop line. If the AV
    stopped, also check if its main decision is to stop for the traffic signal.
    """

    last_localization = Optional[LocalizationEstimate]
    last_traffic_signal_detection = Optional[TrafficLightDetection]
    last_planning = Optional[ADCTrajectory]

    traffic_signal_stop_line_string_dict: Dict[str, LineString]
    violated_at_traffic_signal_ids: Set[str]

    TRAFFIC_LIGHT_VO_ID_PREFIX = "TL_"

    def __init__(self) -> None:
        self.violated_at_traffic_signal_ids = set()

        self.last_localization = None
        self.last_traffic_signal_detection = None
        self.last_planning = None

        self.parse_traffic_signal_stop_line_string_on_map(
            get_map_service_for_map(HD_MAP)
        )

    def get_interested_topics(self):
        """
        The traffic signal oracle is interested in Localization, Traffic Light, and Planning messages.
        Localization messages are used for checking AV's speed and whether it is crossing a stop line,
        Traffic Light messages are used for checking if the AV is facing a red signal, and Planning
        messages are used for checking if the AV made a stop decision for the signal.
        """
        return [
            "/apollo/localization/pose",
            "/apollo/perception/traffic_light",
            "/apollo/planning",
        ]

    def on_new_message(self, topic: str, message, t):
        """
        Upon receiving a new message, the oracle saves the message to analyze later if the AV is
        not crossing a stop line. Once it is crossing a stop line, it checks if it has a positive
        speed. To further gurantee the correctness of this oracle, we also attempt to check whether
        the AV made a complete stop for the signal before crossing the stop line.

        :param str topic: topic of the message
        :param any message: either Planning or Localization message
        :param float t: the timestamp
        """
        if topic == "/apollo/localization/pose":
            self.last_localization = message
        elif topic == "/apollo/perception/traffic_light":
            self.last_traffic_signal_detection = message
            return
        else:
            self.last_planning = message
            return

        if (
            self.last_localization is None
            or self.last_traffic_signal_detection is None
            or self.last_planning is None
        ):
            return

        last_traffic_signal_info = self.last_traffic_signal_detection.traffic_light
        if len(last_traffic_signal_info) <= 0:
            return

        last_traffic_signal_status = last_traffic_signal_info[0].color
        if last_traffic_signal_status != TrafficLight.RED:
            # todo - also handle TrafficLight.BLACK and TrafficLight.UNKNOWN
            return

        last_received_signal_id = last_traffic_signal_info[0].id
        crossing_traffic_signal_id = self.check_if_adc_intersecting_any_stop_lines()
        if last_received_signal_id != crossing_traffic_signal_id:
            return

        # now check both conditions (1) and (2)
        if (
            self.is_planning_main_decision_to_stop_at_traffic_signal(
                self.last_planning, crossing_traffic_signal_id
            )
            is False
            or self.is_adc_completely_stopped() is False
        ):
            self.violated_at_traffic_signal_ids.add(crossing_traffic_signal_id)

    def get_result(self) -> List[Tuple]:
        """
        Returns a list of violations from this oracle
        """
        result = list()
        for traffic_signal_id in self.violated_at_traffic_signal_ids:
            violation = ("traffic_signal", traffic_signal_id)
            result.append(violation)
        return result

    def parse_traffic_signal_stop_line_string_on_map(
        self, map_parser: MapService
    ) -> None:
        """
        Parse and store stop line for every traffic signal on the map
        """
        self.traffic_signal_stop_line_string_dict = dict()
        traffic_signal_ids = map_parser.get_signals()
        for ts_id in traffic_signal_ids:
            traffic_signal_data = map_parser.get_signal_by_id(ts_id)
            line = LineString(
                [
                    [p.x, p.y]
                    for p in traffic_signal_data.stop_line[0]
                    .segment[0]
                    .line_segment.point
                ]
            )
            self.traffic_signal_stop_line_string_dict[ts_id] = line

    def check_if_adc_intersecting_any_stop_lines(self) -> str:
        """
        Check if the AV is intersecting any stop line

        :returns: the ID of the signal controlling that stop line, or empty string
        :rtype: str
        """
        last_localization = self.last_localization
        adc_pose = last_localization.pose
        adc_polygon_pts = generate_adc_polygon(adc_pose.position, adc_pose.heading)
        adc_polygon = Polygon([[x.x, x.y] for x in adc_polygon_pts])
        for (
            traffic_signal_id,
            stop_line_string,
        ) in self.traffic_signal_stop_line_string_dict.items():
            if not stop_line_string.intersection(adc_polygon).is_empty:
                return traffic_signal_id
        return ""

    def is_adc_completely_stopped(self) -> bool:
        """
        Check if the AV is currently stopped

        :returns: True if stopped, False otherwise
        :rtype: bool
        """
        adc_pose = self.last_localization.pose
        adc_velocity = calculate_velocity(adc_pose.linear_velocity)

        # https://github.com/ApolloAuto/apollo/blob/0789b7ea1e1356dde444452ab21b51854781e304/modules/planning/scenarios/stop_sign/unprotected/stage_pre_stop.cc#L237
        # return adc_velocity <= self.MAX_ABS_SPEED_WHEN_STOPPED
        return adc_velocity == 0

    def is_planning_main_decision_to_stop_at_traffic_signal(
        self, planning_message: ADCTrajectory, traffic_signal_id: str
    ) -> bool:
        """
        Check if the AV's main decision is stop for the traffic signal with the specified ID

        :returns: True if a stop decision for the specified signal ID is made, False otherwise
        :rtype: bool
        """
        try:
            stop_decision = planning_message.decision.main_decision.stop
        except AttributeError:
            return False

        stop_reason_code = stop_decision.reason_code
        if stop_reason_code != STOP_REASON_SIGNAL:
            return False

        # e.g,  stop_reason = "stop by SS_stop_sign_0" (included stop_sign_id)
        stop_reason = stop_decision.reason
        if (
            re.sub("^stop by ", "", stop_reason)
            == self.TRAFFIC_LIGHT_VO_ID_PREFIX + traffic_signal_id
        ):
            return True

        return False
