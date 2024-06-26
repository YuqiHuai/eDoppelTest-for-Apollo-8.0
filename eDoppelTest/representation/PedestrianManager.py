import math
from typing import List, Optional, Tuple

from shapely.geometry import LineString, MultiLineString

from apollo.proto_v8.modules.common_msgs.basic_msgs.geometry_pb2 import Point3D
from apollo.utils import pedestrian_location_to_obstacle
from config import HD_MAP
from eDoppelTest.representation.pd_agents import PDAgent, PDSection
from utils import get_map_service_for_map


class PedestrianManager:
    """
    A simplified modeling of constant speed pedestrians

    :param PDSection pedestrians: pedestrians to be managed
    """

    pedestrians: PDSection
    __instance = None
    last_time = 0
    pd_walking_time: List[float]

    def __init__(self, pedestrians: PDSection) -> None:
        """
        Constructor
        """
        self.pedestrians = pedestrians
        self.pd_walking_time = [0.0 for _ in range(len(pedestrians.pds))]
        PedestrianManager.__instance = self

    @staticmethod
    def get_instance() -> "PedestrianManager":
        """
        Returns the singleton instance

        :returns: manager object
        :rtype: PedestrianManager
        """
        return PedestrianManager.__instance

    def calculate_position(
        self, pd: PDAgent, time_spent_walking: float
    ) -> Tuple[Point3D, float]:
        """
        Calculate the pedestrians location and heading at a given time

        :param PDAgent pd: the pedestrian to be calculated
        :param float time_spent_walking: the amount of time pedestrian has traveled for

        :returns: the position and heading
        :rtype: Tuple[Point3D, float]
        """
        # heading is calculated by which segment the pedestrian is on (from the polygon) and then using atan2
        distance = pd.speed * time_spent_walking
        ma = get_map_service_for_map(HD_MAP)
        cw = ma.get_crosswalk_by_id(pd.cw_id)
        cw_boundary = cw.polygon.point
        line_list = []
        for i in range(len(cw_boundary) - 1):
            line_list.append(
                (
                    (cw_boundary[i].x, cw_boundary[i].y),
                    (cw_boundary[i + 1].x, cw_boundary[i + 1].y),
                )
            )
        line_list.append(
            (
                (cw_boundary[-1].x, cw_boundary[-1].y),
                (cw_boundary[0].x, cw_boundary[0].y),
            )
        )
        heading_list = []
        for line in line_list:
            heading_list.append(
                math.atan2(line[1][1] - line[0][1], line[1][0] - line[0][0])
            )
        lines = MultiLineString(line_list)
        boundary_length = lines.length
        curr_point = lines.interpolate(distance % boundary_length)
        for i in range(len(line_list)):
            line = LineString(line_list[i])
            if line.distance(curr_point) < 0.001:
                return Point3D(x=curr_point.x, y=curr_point.y), heading_list[i]
        """
        process the boundary point
        """
        for i in range(len(cw_boundary)):
            x = cw_boundary[i].x
            y = cw_boundary[i].y
            if x == curr_point.x and y == curr_point.y:
                return Point3D(x=curr_point.x, y=curr_point.y), heading_list[i]

    def get_pedestrians(self, curr_time: float) -> List[Tuple[Point3D, float]]:
        """
        Get the location and heading of all pedestrians

        :param float curr_time: time since start of the scenario

        :returns: list consisting position and heading
        :rtype: List[Tuple[Point3D, float]]
        """
        delta_t = curr_time - self.last_time

        result = list()
        for index, pd in enumerate(self.pedestrians.pds):
            if curr_time > pd.start_t:
                self.pd_walking_time[index] += delta_t

            pd_position, heading = self.calculate_position(
                pd, self.pd_walking_time[index]
            )
            p_speed = 0.0 if curr_time < pd.start_t else pd.speed
            result.append(
                pedestrian_location_to_obstacle(index, p_speed, pd_position, heading)
            )
        self.last_time = curr_time
        return result
