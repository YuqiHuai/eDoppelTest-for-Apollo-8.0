# c1 25 -> 49 -> 27
# c2 23 -> 56 -> 27

import time

from apollo import ApolloContainer, ApolloRunner, MapService, MessageBroker
from config import PROJECT_ROOT

map = MapService()
map.load_map_from_file("data/maps/borregas_ave/base_map.bin")
c1, h1 = map.get_lane_coord_and_heading("lane_25", 100)
c2, h2 = map.get_lane_coord_and_heading("lane_23", 5)
c3, h3 = map.get_lane_coord_and_heading("lane_27", 10)


ctn1 = ApolloContainer(
    "data/apollo", "eDoppelTest_test1", "eDoppelTest", PROJECT_ROOT, True
)
ctn2 = ApolloContainer(
    "data/apollo", "eDoppelTest_test2", "eDoppelTest", PROJECT_ROOT, True
)
for ctn in [ctn1, ctn2]:
    ctn.start_container()
    ctn.start_dreamview()
    print(f"http://{ctn.container_ip()}:8888")

runner1 = ApolloRunner(1, ctn1)
runner1.initialze(c1.x, c1.y, h1)

runner2 = ApolloRunner(2, ctn2)
runner2.initialze(c2.x, c2.y, h2)

input("Press enter to initialize message broker")
mb = MessageBroker([runner1, runner2], 10)
mb.spin()

input("Press enter to send routing request")
runner1.send_routing_request(c3.x, c3.y)
runner2.send_routing_request(c3.x, c3.y)
print("Routing request sent")

time.sleep(30)
mb.stop()
runner1.stop()
runner2.stop()
print("Done")
