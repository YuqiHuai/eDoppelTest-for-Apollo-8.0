from typing import List, Tuple

from apollo import MapService, PositionEstimate

from .representation import Scenario, SignalColor, TrafficControl, Vehicle


class ScenarioGenerator:
    def __init__(self, map_service: MapService) -> None:
        self.map_service: MapService = map_service

    def generate_scenario(
        self,
        scenario_id: str,
        routings: List[Tuple[str, str]],
        traffic_control: TrafficControl,
    ) -> Scenario:
        vehicles: List[Vehicle] = list()
        for i, routing in enumerate(routings):
            init_lane, dest_lane = routing
            init_lane_length = self.map_service.get_length_of_lane(init_lane)
            dest_lane_length = self.map_service.get_length_of_lane(dest_lane)
            vehicle = Vehicle(
                i,
                2,
                PositionEstimate(init_lane, round(init_lane_length / 2, 2)),
                PositionEstimate(dest_lane, round(dest_lane_length / 2, 2)),
            )
            vehicles.append(vehicle)
        result = Scenario(scenario_id, vehicles, traffic_control)
        return result

    def generate_traffic_control(self) -> TrafficControl:
        signal_ids = self.map_service.signal_table.keys()
        initial_state = {x: SignalColor.GREEN for x in signal_ids}
        final_state = {x: SignalColor.GREEN for x in signal_ids}
        return TrafficControl(initial_state, final_state, 15, 2, 2)
