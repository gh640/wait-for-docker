"""Wait for Docker to be active."""
import time

import docker
from docker.errors import DockerException


def main():
    while True:
        if check_docker():
            print(" ", end="")
            break

        print(".", end="", flush=True)
        time.sleep(1)

    print("Docker is active now.")


def check_docker() -> bool:
    try:
        docker.from_env()
    except DockerException:
        return False

    return True
