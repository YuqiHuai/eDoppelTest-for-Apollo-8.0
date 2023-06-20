import math
from typing import List, Tuple

from .proto_v8.modules.common_msgs.basic_msgs.geometry_pb2 import Point3D
from .proto_v8.modules.common_msgs.localization_msgs.localization_pb2 import (
    LocalizationEstimate,
)
from .proto_v8.modules.common_msgs.perception_msgs.perception_obstacle_pb2 import (
    PerceptionObstacle,
)

APOLLO_VEHICLE_LENGTH = 4.933
APOLLO_VEHICLE_WIDTH = 2.11
APOLLO_VEHICLE_HEIGHT = 1.48
APOLLO_VEHICLE_back_edge_to_center = 1.043
PERCEPTION_FREQUENCY = 10


def to_Point3D(data: Point3D) -> Point3D:
    """
    Replaces NaN that may occur in Apollo to 0.0

    :param Point3D data: Point3D object to be cleaned

    :returns: cleaned up version of the original Point3D object
    :rtype: Point3D
    """
    return Point3D(
        x=0.0 if math.isnan(data.x) else data.x,
        y=0.0 if math.isnan(data.y) else data.y,
        z=0.0 if math.isnan(data.z) else data.z,
    )


def localization_to_obstacle(
    _id: int, data: LocalizationEstimate
) -> PerceptionObstacle:
    """
    Converts LocalizationEstimate to PerceptionObstacle. The localization
    message of an ADS instance is used as part of the perception message for
    other ADS instances.

    :param int _id: ID of the obstacle
    :param LocalizationEstimate data: localization message of the ADC

    :returns: PerceptionObstacle message converted from localization of an ADC
    :rtype: PerceptionObstacle
    """
    position = to_Point3D(data.pose.position)
    velocity = to_Point3D(data.pose.linear_velocity)
    acceleration = to_Point3D(data.pose.linear_acceleration)

    obs = PerceptionObstacle(
        id=_id,
        position=position,
        theta=data.pose.heading,
        velocity=velocity,
        acceleration=acceleration,
        length=APOLLO_VEHICLE_LENGTH,
        width=APOLLO_VEHICLE_WIDTH,
        height=APOLLO_VEHICLE_HEIGHT,
        type=PerceptionObstacle.VEHICLE,
        timestamp=data.header.timestamp_sec,
        tracking_time=1.0,
        polygon_point=generate_adc_polygon(position, data.pose.heading),
    )
    return obs


def obstacle_to_polygon(obs: PerceptionObstacle) -> List[Tuple[float, float]]:
    """
    Constructs a polygon for an obstacle

    :param PerceptionObstacle obs: the perception obstacle protobuf message

    :returns: a list of tuples representing the polygon
    :rtype: List[Tuple[float, float]]
    """
    return [(p.x, p.y) for p in obs.polygon_point]


def generate_adc_polygon(position: Point3D, theta: float) -> List[Point3D]:
    """
    Generate a polygon for the ADC based on its current position

    :param Point3D position: position of the ADC
    :param float theta: the heading of the ADC (in radians)

    :returns: a list consisting 4 Point3D objects to
        represent ADC polygon
    :rtype: List[Point3D]
    """

    points = []
    half_w = APOLLO_VEHICLE_WIDTH / 2.0
    front_l = APOLLO_VEHICLE_LENGTH - APOLLO_VEHICLE_back_edge_to_center
    back_l = -1 * APOLLO_VEHICLE_back_edge_to_center
    sin_h = math.sin(theta)
    cos_h = math.cos(theta)
    vectors = [
        (front_l * cos_h - half_w * sin_h, front_l * sin_h + half_w * cos_h),
        (back_l * cos_h - half_w * sin_h, back_l * sin_h + half_w * cos_h),
        (back_l * cos_h + half_w * sin_h, back_l * sin_h - half_w * cos_h),
        (front_l * cos_h + half_w * sin_h, front_l * sin_h - half_w * cos_h),
    ]
    for x, y in vectors:
        p = Point3D()
        p.x = position.x + x
        p.y = position.y + y
        p.z = position.z
        points.append(p)
    return points
