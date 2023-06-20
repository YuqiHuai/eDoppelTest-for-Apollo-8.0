import subprocess

from apollo.apollo_container import ApolloContainer
from config import APOLLO_ROOT, PROJECT_NAME, PROJECT_ROOT

if __name__ == "__main__":
    container = ApolloContainer(
        APOLLO_ROOT, f"{PROJECT_NAME}_dev_start", PROJECT_NAME, PROJECT_ROOT, True
    )
    container.start_container(verbose=True)
    container.start_dreamview()
    print(f"Dreamview running at {container.dreamview_url}")
    subprocess.run(
        f"docker exec -u $USER -it {container.container_name} /bin/bash", shell=True
    )
