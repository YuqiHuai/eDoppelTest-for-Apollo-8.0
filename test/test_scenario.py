from apollo import ApolloContainer, MapService
from config import PROJECT_ROOT
from eDoppelTest import ScenarioGenerator, ScenarioRunner

map_service = MapService()
map_service.load_map_from_file("data/maps/borregas_ave/base_map.bin")

scenario_generator = ScenarioGenerator(map_service)

traffic_control = scenario_generator.generate_traffic_control()

routes = [
    ("lane_25", "lane_27"),
    ("lane_23", "lane_27"),
]

scenario = scenario_generator.generate_scenario("test", routes, traffic_control)

ctns = [
    ApolloContainer(
        "data/apollo", "eDoppelTest_test1", "eDoppelTest", PROJECT_ROOT, True
    ),
    ApolloContainer(
        "data/apollo", "eDoppelTest_test2", "eDoppelTest", PROJECT_ROOT, True
    ),
]

for ctn in ctns:
    ctn.start_container()
    ctn.start_dreamview()
    print(f"Dreamview started at http://{ctn.container_ip()}:8888")

scenario_runner = ScenarioRunner(ctns, map_service)
print("First time")
scenario.scenario_id = "test_1"
scenario_runner.run_scenario(scenario, "/eDoppelTest/test_1")
print("Second time")
scenario.scenario_id = "test_2"
scenario_runner.run_scenario(scenario, "/eDoppelTest/test_2")
