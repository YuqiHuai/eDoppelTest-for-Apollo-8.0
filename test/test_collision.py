from eDoppelTest.collision_fitness import CollisionFitness
from cyber_record.record import Record

record = Record(
    "/home/yuqi/ResearchWorkspace/AV_Research/eDoppelTest/out/scenario_1_0.00000"
)

collision_oracle = CollisionFitness()

for channel, msg, t in record.read_messages():
    collision_oracle.on_new_message(channel, msg, t)

print(collision_oracle.get_fitness())
