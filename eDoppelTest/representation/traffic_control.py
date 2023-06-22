from typing import Dict


class SignalColor:
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    RED = "RED"


class TrafficControl:
    def __init__(
        self,
        initial_state: Dict[str, str],
        final_state: Dict[str, str],
        initial_duration: float,
        yellow_duration: float,
        red_duration: float,
    ) -> None:
        self.initial_state: Dict[str, str] = initial_state
        self.final_state: Dict[str, str] = final_state
        self.initial_duration: float = initial_duration
        self.yellow_duration: float = yellow_duration
        self.red_duration: float = red_duration

    def to_json(self) -> Dict:
        return {
            "initial_state": self.initial_state,
            "final_state": self.final_state,
            "initial_duration": self.initial_duration,
            "yellow_duration": self.yellow_duration,
            "red_duration": self.red_duration,
        }

    def __hash__(self) -> int:
        return hash(
            (
                self.initial_state,
                self.final_state,
                self.initial_duration,
                self.yellow_duration,
                self.red_duration,
            )
        )
