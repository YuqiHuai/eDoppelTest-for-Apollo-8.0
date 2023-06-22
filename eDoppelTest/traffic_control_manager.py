from time import time
from typing import Dict

from apollo.proto_v8.modules.common_msgs.perception_msgs.traffic_light_detection_pb2 import (
    TrafficLight,
    TrafficLightDetection,
)

from .representation import SignalColor, TrafficControl


class TrafficControlManager:
    def __init__(self, traffic_control: TrafficControl) -> None:
        self.traffic_control: TrafficControl = traffic_control
        self.tld_sequence_number: int = 0

    def get_traffic_light_detection_message_at_t(
        self, t: float
    ) -> TrafficLightDetection:
        self.tld_sequence_number += 1
        color_assignment = self.get_signal_colors_at_t(t)

        tld = TrafficLightDetection()
        tld.header.timestamp_sec = time()
        tld.header.module_name = "eDoppelTest"
        tld.header.sequence_num = self.tld_sequence_number

        for signal_id, color in color_assignment.items():
            tl = tld.traffic_light.add()
            tl.id = signal_id
            tl.confidence = 1.0

            if color == SignalColor.GREEN:
                tl.color = TrafficLight.GREEN
            elif color == SignalColor.YELLOW:
                tl.color = TrafficLight.YELLOW
            else:
                tl.color = TrafficLight.RED

        return tld

    def has_transition(self, signal_id: str) -> bool:
        return (
            self.traffic_control.initial_state[signal_id] == SignalColor.GREEN
            and self.traffic_control.final_state[signal_id] == SignalColor.RED
        )

    def get_signal_colors_at_t(self, t: float) -> Dict[str, str]:
        result: Dict[str, str] = dict()
        if t < self.traffic_control.initial_duration:
            return self.traffic_control.initial_state
        elif t < (
            self.traffic_control.initial_duration + self.traffic_control.yellow_duration
        ):
            for signal_id, color in self.traffic_control.initial_state.items():
                if self.has_transition(signal_id):
                    result[signal_id] = SignalColor.YELLOW
                else:
                    result[signal_id] = color
            return result
        elif t < (
            self.traffic_control.initial_duration
            + self.traffic_control.yellow_duration
            + self.traffic_control.red_duration
        ):
            for signal_id, color in self.traffic_control.initial_state.items():
                if self.has_transition(signal_id):
                    result[signal_id] = SignalColor.RED
                else:
                    result[signal_id] = color
            return result
        else:
            return self.traffic_control.final_state
