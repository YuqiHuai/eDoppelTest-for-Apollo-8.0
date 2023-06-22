import threading
import time
from decimal import Decimal
from typing import List

from apollo import ApolloContainer, ApolloRunner, Channels, MapService, MessageBroker

from .representation import Scenario
from .traffic_control_manager import TrafficControlManager


class ScenarioRunner:
    def __init__(
        self, containers: List[ApolloContainer], map_service: MapService
    ) -> None:
        self.containers: List[ApolloContainer] = containers
        self.map_service = map_service

    def _initialize_containers(self, scenario: Scenario) -> List[ApolloRunner]:
        runners: List[ApolloRunner] = []

        initialize_threads: List[threading.Thread] = []

        for i, ctn in enumerate(self.containers):
            runner = ApolloRunner(i, ctn)
            runners.append(runner)

            initial_position = scenario.vehicles[i].initial_position
            final_position = scenario.vehicles[i].final_position

            (
                initial_coord,
                initial_heading,
            ) = self.map_service.get_lane_coord_and_heading(
                initial_position.lane_id, initial_position.s
            )

            (
                final_coord,
                _,
            ) = self.map_service.get_lane_coord_and_heading(
                final_position.lane_id, final_position.s
            )
            runner.set_destination(final_coord.x, final_coord.y)

            initialize_threads.append(
                threading.Thread(
                    target=runner.initialze,
                    args=(
                        initial_coord.x,
                        initial_coord.y,
                        initial_heading,
                    ),
                )
            )

        for thread in initialize_threads:
            thread.start()

        for thread in initialize_threads:
            thread.join()

        return runners

    def run_scenario(self, scenario: Scenario, record_prefix=""):
        assert len(self.containers) == len(
            scenario.vehicles
        ), "Number of containers must match number of vehicles in scenario"
        if record_prefix:
            assert record_prefix.startswith(
                "/"
            ), "record_prefix must be an absolute path"
        traffic_control_manager = TrafficControlManager(scenario.traffic_control)
        runners = self._initialize_containers(scenario)
        mb = MessageBroker(runners)
        mb.spin()

        if record_prefix:
            for i, ctn in enumerate(self.containers):
                ctn.start_recorder(f"{record_prefix}_{i}")

        # scenario logic
        scenario_current_time = 0.0  # s
        scenario_duration = 30.0  # s
        time_increment = 0.1  # ms
        while scenario_current_time <= scenario_duration:
            if scenario_current_time - int(scenario_current_time) == 0:
                mb.broadcast(
                    Channels.TrafficLight,
                    traffic_control_manager.get_traffic_light_detection_message_at_t(
                        scenario_current_time
                    ).SerializeToString(),
                )
            for i, vehicle in enumerate(scenario.vehicles):
                if vehicle.idle_time == scenario_current_time:
                    runners[i].send_routing_request()
            time.sleep(time_increment)
            scenario_current_time = round(scenario_current_time + time_increment, 2)

        if record_prefix:
            for ctn in self.containers:
                ctn.stop_recorder()

        mb.stop()
        for runner in runners:
            runner.stop()
