import time
from threading import Thread
from typing import Dict, List, Optional

from .apollo_runner import ApolloRunner
from .cyber_bridge import Channel, Channels
from .proto_v8.modules.common_msgs.basic_msgs.header_pb2 import Header
from .proto_v8.modules.common_msgs.localization_msgs.localization_pb2 import (
    LocalizationEstimate,
)
from .proto_v8.modules.common_msgs.perception_msgs.perception_obstacle_pb2 import (
    PerceptionObstacles,
)
from .utils import localization_to_obstacle


class MessageBroker:
    """
    Class to represent MessageBroker, it tracks location of each
    ADS instance and broadcasts perception message to all ADS instances
    """

    def __init__(self, runners: List[ApolloRunner], forward_frequency=10) -> None:
        """
        Constructor
        """
        self.runners: List[ApolloRunner] = runners
        self.forward_frequency: int = forward_frequency
        self.spinning: bool = False
        self._thread: Optional[Thread] = None

    def broadcast(self, channel: Channel, data: bytes):
        """
        Sends data to specified channel of every instance

        :param Channel channel: cyberRT channel to send data to
        :param bytes data: data to be sent
        """
        for runner in self.runners:
            if runner.container.bridge:
                runner.container.bridge.publish(channel, data)

    def _spin(self) -> None:
        """
        Helper function to start forwarding localization
        """
        header_sequence_num = 0
        curr_time = 0.0
        while self.spinning:
            # retrieve localization of running instances
            locations: Dict[int, LocalizationEstimate] = dict()
            for runner in self.runners:
                if runner.last_localization:
                    locations[runner.rid] = runner.last_localization

            # convert localization into obstacles
            obs = dict()
            for k in locations:
                obs[k] = localization_to_obstacle(k, locations[k])

            # publish obstacle to all running instances
            for runner in self.runners:
                perception_obs = [obs[x] for x in obs if x != runner.rid]
                header = Header(
                    timestamp_sec=time.time(),
                    module_name="eDoppelTest",
                    sequence_num=header_sequence_num,
                )
                bag = PerceptionObstacles(
                    header=header,
                    perception_obstacle=perception_obs,
                )
                assert runner.container.bridge, "Bridge is not initialized"
                runner.container.bridge.publish(
                    Channels.Obstacles, bag.SerializeToString()
                )
            header_sequence_num += 1
            time.sleep(1 / self.forward_frequency)
            curr_time += 1 / self.forward_frequency

    def spin(self):
        """
        Starts to forward localization
        """
        if self.spinning:
            return
        self._thread = Thread(target=self._spin)
        self.spinning = True
        self._thread.start()

    def stop(self):
        """
        Stops forwarding localization
        """
        if not self.spinning or not self._thread:
            return
        self.spinning = False
        self._thread.join()
        self._thread = None
