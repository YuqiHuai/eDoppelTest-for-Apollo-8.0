# 25 -> 49 -> 27
import time

from apollo import ApolloContainer, ApolloRunner, MapService
from config import PROJECT_ROOT

map = MapService()
map.load_map_from_file("data/maps/borregas_ave/base_map.bin")
c1, h1 = map.get_lane_coord_and_heading("lane_25", 50)
c2, h2 = map.get_lane_coord_and_heading("lane_27", 10)


ctn = ApolloContainer(
    "data/apollo", "eDoppelTest_test", "eDoppelTest", PROJECT_ROOT, True
)
ctn.start_container()
ctn.start_dreamview()
print("Dreamview started")
print(f"http://{ctn.container_ip()}:8888")
runner = ApolloRunner(1, ctn)
runner.initialze(c1.x, c1.y, h1)
input("Press enter to send routing request")
runner.send_routing_request(c2.x, c2.y)
time.sleep(30)
runner.stop()
print("Done")
