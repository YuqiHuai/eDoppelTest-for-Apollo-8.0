import threading
import time
from logging import Logger
from pathlib import Path
from typing import List, Optional, Tuple

from loguru import logger

from apollo.apollo_container import ApolloContainer
from apollo.apollo_runner import ApolloRunner
from apollo.cyber_bridge import Channels
from apollo.message_broker import MessageBroker
from apollo.proto_v8.modules.common_msgs.map_msgs.map_pb2 import Map
from apollo.utils import clean_appolo_dir
from config import APOLLO_ROOT, SCENARIO_UPPER_LIMIT
from eDoppelTest.representation import Scenario
from eDoppelTest.representation.ad_agents import ADAgent
from eDoppelTest.representation.PedestrianManager import PedestrianManager
from eDoppelTest.representation.TrafficControlManager import TrafficControlManager
from utils import random_numeric_id


class ScenarioRunner:
    """
    Executes a scenario based on the specification

    :param List[ApolloContainer] containers: containers to be used for scenario
    """

    logger: Logger
    containers: List[ApolloContainer]
    curr_scenario: Optional[Scenario]
    pm: Optional[PedestrianManager]
    tm: Optional[TrafficControlManager]
    is_initialized: bool
    __instance = None

    __runners: List[ApolloRunner]

    def __init__(self, containers: List[ApolloContainer]) -> None:
        """
        Constructor
        """
        self.logger = logger
        self.containers = containers
        self.curr_scenario = None
        self.is_initialized = False
        ScenarioRunner.__instance = self

    @staticmethod
    def get_instance() -> "ScenarioRunner":
        """
        Returns the singleton instance

        :returns: an instance of runner
        :rtype: ScenarioRunner
        """
        return ScenarioRunner.__instance

    def set_scenario(self, s: Scenario):
        """
        Set the scenario for this runner

        :param Scenario s: scenario representation
        """
        self.curr_scenario = s
        self.is_initialized = False

    def init_scenario(self):
        """
        Initialize the scenario
        """
        nids = random_numeric_id(len(self.curr_scenario.ad_section.adcs))
        self.__runners = list()
        for i, c, a in zip(nids, self.containers, self.curr_scenario.ad_section.adcs):
            a.apollo_container = c.container_name
            self.__runners.append(
                ApolloRunner(
                    nid=i,
                    ctn=c,
                    start=a.initial_position,
                    waypoints=a.waypoints,
                    start_time=a.start_t,
                )
            )

        # initialize Apollo instances
        threads = list()
        for index in range(len(self.__runners)):
            threads.append(threading.Thread(target=self.__runners[index].initialize))
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        # remove Apollo logs
        clean_appolo_dir(APOLLO_ROOT)

        # initialize pedestrian and traffic control manager
        self.pm = PedestrianManager(self.curr_scenario.pd_section)
        self.tm = TrafficControlManager(self.curr_scenario.tc_section)
        self.is_initialized = True

    def run_scenario(self, record_prefix="") -> List[Tuple[ApolloRunner, ADAgent]]:
        """
        Execute the scenario based on the specification

        :param str generation_name: name of the generation
        :param str scenario_name: name of the scenario
        :param bool save_record: whether to save records or not
        """
        num_adc = len(self.curr_scenario.ad_section.adcs)
        self.logger.info(
            f"{num_adc} agents running a scenario G{self.curr_scenario.gid}S{self.curr_scenario.cid}."
        )
        if self.curr_scenario is None or not self.is_initialized:
            print("Error: No chromosome or not initialized")
            return

        mbk = MessageBroker(self.__runners)
        mbk.spin()

        runner_time = 0
        # starting scenario
        if record_prefix:
            for i, r in enumerate(self.__runners):
                r.container.start_recorder(
                    Path(record_prefix, r.container.container_name)
                )

        # Begin Scenario Cycle
        while True:
            # Publish TrafficLight
            tld = self.tm.get_traffic_configuration(runner_time / 1000)
            mbk.broadcast(Channels.TrafficLight, tld.SerializeToString())

            # Send Routing
            for ar in self.__runners:
                if ar.should_send_routing(runner_time / 1000):
                    ar.send_routing()

            # Check if scenario exceeded upper limit
            if runner_time / 1000 >= SCENARIO_UPPER_LIMIT:
                break

            time.sleep(0.1)
            runner_time += 100

        if record_prefix:
            for r in self.__runners:
                r.container.stop_recorder()
            # buffer period for recorders to stop
            time.sleep(2)
            # save_record_files_and_chromosome(
            #     generation_name, scenario_name, self.curr_scenario.to_dict())
        # scenario ended
        mbk.stop()
        for runner in self.__runners:
            runner.stop("MAIN")

        self.logger.debug(
            f"Scenario ended. Length: {round(runner_time/1000, 2)} seconds."
        )

        self.is_initialized = False

        return list(zip(self.__runners, self.curr_scenario.ad_section.adcs))
