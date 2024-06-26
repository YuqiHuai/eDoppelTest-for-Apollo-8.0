import os
import subprocess
import time
from pathlib import Path
from typing import Optional

import docker
import docker.errors

from .cyber_bridge import CyberBridge

CURR_DIRR = Path(__file__).parent


class ApolloContainer:
    def __init__(
        self,
        apollo_dir: Path,
        ctn_name: str,
        project_name: str,
        project_root: Path,
        allow_multiple=False,
    ) -> None:
        self.apollo_dir: Path = apollo_dir
        self.ctn_name: str = ctn_name
        self.project_name: str = project_name
        self.project_root: Path = project_root
        self.allow_multiple: bool = allow_multiple
        self.bridge: Optional[CyberBridge] = None

    def __repr__(self):
        return f"ApolloContainer(ctn_name={repr(self.ctn_name)})"

    def start_container(self, verbose=False):
        if self.is_running():
            return True
        options = "-y -l -f"
        docker_script_dir = Path(self.apollo_dir, "docker", "scripts")
        if self.allow_multiple:
            start_script = Path(CURR_DIRR, "scripts", "multi_ctn_dev_start.sh")
        else:
            start_script = Path(CURR_DIRR, "scripts", "dev_start.sh")
        cmd = f"bash {start_script} {options}"
        subprocess.run(
            cmd,
            env={
                "CURR_DIR": docker_script_dir,
                "DEV_CONTAINER": self.ctn_name,
                "USER": os.environ.get("USER"),
                "PROJECT_ROOT": self.project_root.absolute(),
                "PROJECT_NAME": f"/{self.project_name}",
            },
            shell=True,
            capture_output=not verbose,
        )

    def rm_container(self):
        if self.is_running():
            for op in ["stop", "rm"]:
                cmd = f"docker {op} {self.container_name}"
                subprocess.run(cmd, shell=True, capture_output=True)

    @property
    def container_name(self) -> str:
        return self.ctn_name

    def container_ip(self) -> str:
        """
        Gets the ip address of the container
        :returns: IP address of this container
        """
        assert self.is_running(), f"Container {self.container_name} is not running."
        ctn = docker.from_env().containers.get(self.container_name)
        return ctn.attrs["NetworkSettings"]["IPAddress"]

    def exists(self) -> bool:
        """
        Checks if the container exists
        :returns: True if exists, False otherwise
        """
        try:
            docker.from_env().containers.get(self.container_name)
            return True
        except (docker.errors.NotFound, docker.errors.DockerException):
            return False

    def is_running(self) -> bool:
        """
        Checks if the container is running
        :returns: True if running, False otherwise
        """
        try:
            return (
                docker.from_env().containers.get(self.container_name).status
                == "running"
            )
        except Exception:
            return False

    @property
    def dreamview_url(self) -> str:
        """
        Gets the Dreamview url of the container
        :returns: Dreamview url of this container
        """
        return f"http://{self.container_ip()}:8888"

    def exec(self, cmd: str, detached=False, verbose=False):
        """
        Executes a command in the container
        :param cmd: Command to execute
        :param detached: Whether the command should be executed in detached mode
        """
        exe = (
            "docker exec "
            + "-u $USER "
            + f'{"-d " if detached else ""}{self.container_name} {cmd}'
        )
        return subprocess.run(exe, shell=True, capture_output=not verbose)

    def start_dreamview(self):
        self.exec("bash /apollo/scripts/dreamview.sh start")

    def restart_dreamview(self):
        self.exec("bash /apollo/scripts/dreamview.sh restart")

    def start_bridge(self):
        self.exec("bash /apollo/scripts/bridge.sh", detached=True)
        ip_address = self.container_ip()
        if ip_address != "":
            trial = 0
            max_trial = 3
            while trial < 3:
                try:
                    self.bridge = CyberBridge(ip_address)
                    return
                except ConnectionRefusedError:
                    time.sleep(0.5)
                    trial += 1
            raise ConnectionRefusedError(
                f"Cannot connect to CyberBridge after {max_trial} trials."
            )

    def start_planning(self):
        self.exec("bash /apollo/scripts/planning.sh start")

    def start_routing(self):
        self.exec("bash /apollo/scripts/routing.sh start")

    def start_prediction(self):
        self.exec("bash /apollo/scripts/prediction.sh start")

    def start_ads_modules(self):
        # self.start_bridge()
        self.start_routing()
        self.start_prediction()
        self.start_planning()

    def stop_ads_modules(self):
        cmd = "pkill --signal SIGKILL -f 'planning|routing|prediction|cyber_bridge'"
        self.exec(cmd)
        self.bridge = None

    def start_sim_control(self, x: float, y: float, heading: float):
        executable = "/apollo/bazel-bin/modules/sim_control_standalone/main"
        cmd = f"{executable} {x} {y} {heading}"
        self.exec(cmd, detached=True)

    def stop_sim_control(self):
        cmd = "pkill --signal SIGKILL -f 'sim_control_standalone'"
        self.exec(cmd)

    def start_replay(self, filename: str):
        # cyber_recorder play -f <file>
        cyber_recorder = "/apollo/bazel-bin/cyber/tools/cyber_recorder/cyber_recorder"
        cmd = f"{cyber_recorder} play -f {filename}"
        self.exec(cmd, detached=True)

    def stop_replay(self):
        cmd = "pkill --signal SIGINT -f 'cyber_recorder play'"
        self.exec(cmd)

    def start_recorder(self, filename: str):
        # cyber_recorder record -o <file>
        cyber_recorder = "/apollo/bazel-bin/cyber/tools/cyber_recorder/cyber_recorder"
        cmd = f"{cyber_recorder} record -a -o {filename}"
        self.exec(cmd, detached=True)

    def stop_recorder(self):
        cmd = "pkill --signal SIGINT -f 'cyber_recorder record'"
        self.exec(cmd)
