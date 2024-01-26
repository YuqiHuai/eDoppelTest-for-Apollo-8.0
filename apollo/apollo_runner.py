from logging import Logger
import time
from typing import List, Optional, Set, Tuple

from loguru import logger
from apollo.map_service import PositionEstimate
from apollo.proto_v8.modules.common_msgs.planning_msgs.planning_pb2 import ADCTrajectory
from apollo.utils import extract_main_decision
from config import HD_MAP

from utils import get_map_service_for_map

from .apollo_container import ApolloContainer
from .cyber_bridge import Channels
from .proto_v8.modules.common_msgs.basic_msgs.geometry_pb2 import PointENU
from .proto_v8.modules.common_msgs.basic_msgs.header_pb2 import Header
from .proto_v8.modules.common_msgs.localization_msgs.localization_pb2 import (
    LocalizationEstimate,
)
from .proto_v8.modules.common_msgs.routing_msgs.routing_pb2 import (
    LaneWaypoint,
    RoutingRequest,
)


class ApolloRunner:
    logger: Logger
    nid: int
    container: ApolloContainer
    start: PositionEstimate
    start_time: float
    waypoints: List[PositionEstimate]
    routing_started: bool
    stop_time_counter: float
    localization: Optional[LocalizationEstimate]
    planning: Optional[ADCTrajectory]
    __min_distance: Optional[float]
    __decisions: Set[Tuple]
    __coords: List[Tuple]

    def __init__(self,
                 nid: int,
                 ctn: ApolloContainer,
                 start: PositionEstimate,
                 start_time: float,
                 waypoints: List[PositionEstimate]
                 ) -> None:
        """
        Constructor
        """
        self.logger = logger
        self.nid = nid
        self.container = ctn
        self.start = start
        self.start_time = start_time
        self.waypoints = waypoints

    def register_publishers(self):
        assert self.container is not None, "Bridge not initialized"
        for channel in [
            Channels.RoutingRequest,
            Channels.Obstacles,
            Channels.TrafficLight,
        ]:
            self.container.bridge.add_publisher(channel)

    def register_subscribers(self):
        """
        Register subscribers for the cyberRT communication
        """
        def lcb(data):
            """
            Callback function when localization message is received
            """
            self.localization = data
            self.__coords.append((data.pose.position.x, data.pose.position.y))

        def pcb(data):
            """
            Callback function when planning message is received
            """
            self.planning = data
            decisions = extract_main_decision(data)
            self.__decisions.update(decisions)

        self.container.bridge.add_subscriber(Channels.Localization, lcb)
        self.container.bridge.add_subscriber(Channels.Planning, pcb)


    def initialize(self):
        self.container.stop_ads_modules()
        self.container.stop_sim_control()
        self.container.start_ads_modules()
        map_service = get_map_service_for_map(HD_MAP)
        point, heading = map_service.get_lane_coord_and_heading(
            self.start.lane_id, self.start.s
        )
        self.container.start_sim_control(point.x, point.y, heading)
        self.container.start_bridge()
        assert self.container.bridge, "Bridge not initialized"
        self.container.bridge.spin()
        self.register_publishers()
        self.register_subscribers()

        self.routing_started = False
        self.__min_distance = None
        self.__decisions = set()
        self.__coords = list()
        self.planning = None
        self.localization = None

    def set_destination(self, x: float, y: float):
        self.dest_x = x
        self.dest_y = y

    def send_routing_request(self):
        assert self.container.bridge, "Bridge not initialized"
        assert (
            self.dest_x is not None and self.dest_y is not None
        ), "Destination not set"
        current_x = self.localization.pose.position.x
        current_y = self.localization.pose.position.y
        current_heading = self.localization.pose.heading


        routing_request = RoutingRequest(
            header=Header(
                timestamp_sec=time.time(),
                module_name="eDoppelTest",
                sequence_num=0,
            ),
            waypoint=[
                LaneWaypoint(
                    pose=PointENU(x=current_x, y=current_y, z=0.0),
                    heading=current_heading,
                ),
                LaneWaypoint(
                    pose=PointENU(x=self.dest_x, y=self.dest_y, z=0.0),
                ),
            ],
        )
        self.container.bridge.publish(
            Channels.RoutingRequest, routing_request.SerializeToString()
        )

    def stop(self, stop_reason: str):
        self.container.bridge.stop()
        self.container.stop_ads_modules()
        self.container.stop_sim_control()
        self.logger.debug(f"Runner {self.nid} stopped: {stop_reason}")

    def should_send_routing(self, t: float) -> bool:
        """
        Check if a routing request should be send to the Apollo instance

        :param float t: the amount of time since the start of the simulation

        :returns: True if should send, False otherwise
        :rtype: bool
        """
        return t >= self.start_time and not self.routing_started
    
    def send_routing(self):
        """
        Send the instance's routing request to cyberRT
        """
        self.logger.debug(
            f'Sending routing request to {self.container.container_name}')
        self.routing_started = True
        ma = get_map_service_for_map(HD_MAP)
        coord, heading = ma.get_lane_coord_and_heading(
            self.start.lane_id, self.start.s)

        rr = RoutingRequest(
            header=Header(
                timestamp_sec=time.time(),
                module_name="eDoppelTest",
                sequence_num=0
            ),
            waypoint=[
                LaneWaypoint(
                    pose=PointENU(x=coord.x, y=coord.y, z=0.0),
                    heading=heading
                )
            ] + [
                LaneWaypoint(
                    id=x.lane_id,
                    s=x.s,
                ) for x in self.waypoints
            ]
        )

        self.container.bridge.publish(
            Channels.RoutingRequest, rr.SerializeToString()
        )

    def get_decisions(self) -> Set[Tuple]:
        """
        Get the decisions made by the Apollo instance

        :returns: list of decisions made
        :rtype: Set[Tuple]
        """
        return self.__decisions

    def get_trajectory(self) -> List[Tuple]:
        """
        Get the points traversed by this Apollo instance

        :returns: list of coordinates traversed by this Apollo instance
        :rtype: List[Tuple[float, float]]
        """
        return self.__coords

    def get_min_distance(self) -> float:
        """
        Get the minimum distance this instance ever reached w.r.t. another
        object. e.g., 0 if a collision occurred

        :returns: the minimum distance between this Apollo instance and another object
        :rtype: float
        """
        if not self.__min_distance:
            return 10000
        return self.__min_distance
