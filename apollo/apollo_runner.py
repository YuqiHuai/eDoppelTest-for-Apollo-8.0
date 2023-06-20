import time
from typing import Optional

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
    def __init__(self, aid: int, ctn: ApolloContainer) -> None:
        self.aid = aid
        self.container = ctn
        self.last_localization: Optional[LocalizationEstimate] = None

    def register_publishers(self):
        assert self.container is not None, "Bridge not initialized"
        for channel in [
            Channels.RoutingRequest,
            Channels.Obstacles,
            Channels.TrafficLight,
        ]:
            self.container.bridge.add_publisher(channel)

    def register_subscribers(self):
        def lcb(data: LocalizationEstimate):
            self.last_localization = data

        self.container.bridge.add_subscriber(Channels.Localization, lcb)

    def initialze(self, x: float, y: float, heading: float):
        self.container.stop_ads_modules()
        self.container.stop_sim_control()
        self.container.start_ads_modules()
        self.container.start_sim_control(x, y, heading)
        self.container.start_bridge()
        self.container.bridge.spin()
        self.register_publishers()
        self.register_subscribers()

    def send_routing_request(self, target_x: float, target_y: float):
        assert self.last_localization, "Localization not received"
        assert self.container.bridge, "Bridge not initialized"

        current_x = self.last_localization.pose.position.x
        current_y = self.last_localization.pose.position.y
        current_heading = self.last_localization.pose.heading

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
                    pose=PointENU(x=target_x, y=target_y, z=0.0),
                ),
            ],
        )
        self.container.bridge.publish(
            Channels.RoutingRequest, routing_request.SerializeToString()
        )

    def stop(self):
        self.container.bridge.stop()
        self.container.stop_ads_modules()
        self.container.stop_sim_control()
