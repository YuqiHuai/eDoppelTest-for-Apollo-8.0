from dataclasses import dataclass

from apollo.map_service import PositionEstimate


@dataclass
class Vehicle:
    vid: int
    idle_time: float
    initial_position: PositionEstimate
    final_position: PositionEstimate

    def __post_init__(self):
        self.idle_time = round(self.idle_time, 2)

    def __hash__(self) -> int:
        return hash(
            (
                self.vid,
                self.idle_time,
                self.initial_position,
                self.final_position,
            )
        )

    def to_json(self):
        return {
            "vid": self.vid,
            "idle_time": self.idle_time,
            "initial_position": self.initial_position.to_json(),
            "final_position": self.final_position.to_json(),
        }
