from pathlib import Path
from random import random

from cyber_record.record import Record
from deap import algorithms, base, tools

from apollo import ApolloContainer, MapService
from config import APOLLO_ROOT, PROJECT_NAME, PROJECT_ROOT
from eDoppelTest import ScenarioGenerator, ScenarioRunner
from eDoppelTest.collision_fitness import CollisionFitness
from eDoppelTest.genetic_operators import GeneticOperators
from eDoppelTest.representation import Scenario

routes = [
    ("lane_23", "lane_27"),  # left turn
    ("lane_25", "lane_27"),  # right turn
]

target_dir = Path(PROJECT_ROOT, "out", "scenario_1")
if not target_dir.exists():
    target_dir.mkdir(parents=True)

map_service = MapService()
map_service.load_map_from_file("data/maps/borregas_ave/base_map.bin")

scenario_generator = ScenarioGenerator(map_service)
traffic_control = scenario_generator.generate_traffic_control()
scenario = scenario_generator.generate_scenario("test", routes, traffic_control)

containers = []
for i in range(len(routes)):
    containers.append(
        ApolloContainer(
            APOLLO_ROOT, f"eDoppelTest_{i}", PROJECT_NAME, PROJECT_ROOT, True
        )
    )

for container in containers:
    container.start_container()
    container.start_dreamview()
    print(f"Dreamview started at http://{container.container_ip()}:8888")

runner = ScenarioRunner(containers, map_service)

# ==============================================================================


def evaluate(generation: int, ind: Scenario, scenario_runner: ScenarioRunner):
    path_segments = ["out", "scenario_1", f"g{generation}", ind.scenario_id]
    host_path = Path(PROJECT_ROOT, *path_segments)
    if not host_path.parent.exists():
        host_path.parent.mkdir(parents=True)
    in_dev_path = Path(f"/{PROJECT_NAME}", *path_segments)
    scenario_runner.run_scenario(ind, str(in_dev_path))
    record_file = Path(host_path.parent, f"{ind.scenario_id}_0.00000")
    collision_fitness = CollisionFitness()
    record = Record(record_file)
    for topic, msg, t in record.read_messages():
        collision_fitness.on_new_message(topic, msg, t)
    ind.fitness.values = (collision_fitness.get_fitness(),)


pop_size = 15
gen = 0
genetic_operators = GeneticOperators(map_service)
population = [
    scenario_generator.generate_scenario(f"g{gen}s{i:02}", routes, traffic_control)
    for i in range(pop_size)
]
for ind in population:
    genetic_operators.mutate(ind)
    evaluate(gen, ind, runner)
    print(f"Gen {gen} scenario {ind.scenario_id} fitness: {ind.fitness.values[0]}")

toolbox = base.Toolbox()
toolbox.register("mate", genetic_operators.cross_over)
toolbox.register("mutate", genetic_operators.mutate)
toolbox.register("select", tools.selBest)

while True:
    gen += 1
    offsprings = algorithms.varAnd(population, toolbox, 0.8, 0.2)
    for index, ind in enumerate(offsprings):
        ind.scenario_id = f"g{gen}s{index:02}"
        evaluate(gen, ind, runner)
        print(f"Gen {gen} scenario {ind.scenario_id} fitness: {ind.fitness.values[0]}")

    population = toolbox.select(population + offsprings, len(population))
    best = tools.selBest(offsprings, 1)[0]
    fitness_values = [ind.fitness.values[0] for ind in offsprings]

    with open(Path(PROJECT_ROOT, "out", "scenario_1", "summary.txt"), "a") as f:
        for ind in offsprings:
            if ind.fitness.values[0] == 0.0:
                f.write(f"{ind.scenario_id}\n")

    print("=" * 20)
    print(f"Generation {gen}: {best.fitness.values[0]}")
    print(fitness_values)
    print("=" * 20)
    # a third of the population has a fitness value of 0.0
    if fitness_values.count(0.0) > pop_size / 3:
        break
