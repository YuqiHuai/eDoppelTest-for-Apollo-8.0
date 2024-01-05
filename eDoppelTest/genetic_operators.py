from .representation import Scenario
from apollo import MapService
from random import random, choice, randint
from copy import deepcopy

from typing import Tuple


class GeneticOperators:
    def __init__(self, map_service: MapService) -> None:
        self.map_service = map_service

    def _align_idle_times(self, scenario: Scenario):
        idle_times = [v.idle_time for v in scenario.vehicles]
        diff = min(idle_times) - 2
        if diff != 0:
            for v in scenario.vehicles:
                v.idle_time -= diff

    def _correct_start_s(self, scenario: Scenario):
        for vehicle in scenario.vehicles:
            lane_length = self.map_service.get_length_of_lane(
                vehicle.initial_position.lane_id
            )
            if lane_length < 5:
                vehicle.initial_position.s = 0
            elif vehicle.initial_position.s > lane_length - 5:
                vehicle.initial_position.s = max(0, lane_length - 5)

    def mutate(self, scenario: Scenario) -> Tuple[Scenario,]:
        result = deepcopy(scenario)
        vehicle = choice(result.vehicles)
        if random() < 0.3:
            # mutate start time
            vehicle.idle_time = randint(2, 10)
        else:
            # mutate start position
            lane_length = self.map_service.get_length_of_lane(
                vehicle.initial_position.lane_id
            )
            if lane_length < 5:
                vehicle.initial_position.s = 0
            else:
                vehicle.initial_position.s = round(random() * (lane_length - 5), 2)

        # make sure min(idle_time) == 2
        self._align_idle_times(result)
        return (result,)

    def cross_over(
        self, scenario1: Scenario, scenario2: Scenario
    ) -> Tuple[Scenario, Scenario]:
        lhs = deepcopy(scenario1)
        rhs = deepcopy(scenario2)

        if random() < 0.5:
            # cross over a vehicle
            vehicle_index = choice(range(len(lhs.vehicles)))
            lhs.vehicles[vehicle_index], rhs.vehicles[vehicle_index] = (
                rhs.vehicles[vehicle_index],
                lhs.vehicles[vehicle_index],
            )
        else:
            # cross over start time / position
            vehicle_index = choice(range(len(lhs.vehicles)))

            if random() < 0.5:
                # cross over start time
                (
                    lhs.vehicles[vehicle_index].idle_time,
                    rhs.vehicles[vehicle_index].idle_time,
                ) = (
                    rhs.vehicles[vehicle_index].idle_time,
                    lhs.vehicles[vehicle_index].idle_time,
                )
            else:
                # cross over start position
                l_initial_s = lhs.vehicles[vehicle_index].initial_position.s
                r_initial_s = rhs.vehicles[vehicle_index].initial_position.s

                lhs.vehicles[vehicle_index].initial_position.s = r_initial_s
                rhs.vehicles[vehicle_index].initial_position.s = l_initial_s

                # make sure start position is still valid
                self._correct_start_s(lhs)
                self._correct_start_s(rhs)

        self._align_idle_times(lhs)
        self._align_idle_times(rhs)
        return lhs, rhs
