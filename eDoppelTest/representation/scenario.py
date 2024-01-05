from dataclasses import dataclass, field
from typing import List
from deap import base
from .traffic_control import TrafficControl
from .vehicle import Vehicle


class ScenarioFitness(base.Fitness):
    weights = (-1.0,)


@dataclass
class Scenario:
    scenario_id: str
    vehicles: List[Vehicle]
    traffic_control: TrafficControl

    fitness: base.Fitness = field(default_factory=ScenarioFitness)

    def __hash__(self) -> int:
        return hash((self.scenario_id, tuple(self.vehicles)))

    def to_json(self):
        return {
            "scenario_id": self.scenario_id,
            "vehicles": [v.to_json() for v in self.vehicles],
            "traffic_control": self.traffic_control.to_json(),
        }
