"""Wait for Docker to be active."""
import time

import docker
from docker.errors import DockerException
from yaspin import yaspin


def main():
    with yaspin():
        while not check_docker():
            time.sleep(0.5)

    print("Docker is active now.")


def check_docker() -> bool:
    try:
        docker.from_env()
    except DockerException:
        return False

    return True
