import time

import docker
import pytest
from docker.errors import DockerException
from wait_for_docker import __version__, main


def test_version():
    assert __version__ == '0.2.0'


def test_main_return_imediately(mocker):
    check_docker = mocker.patch('wait_for_docker.main.check_docker')
    sleep = mocker.patch('time.sleep')
    check_docker.return_value = True

    assert check_docker.called is False

    main.main()

    assert check_docker.called is True
    assert check_docker.call_count == 1
    assert sleep.called is False


def test_main_loop(mocker):
    check_docker = mocker.patch('wait_for_docker.main.check_docker')
    sleep = mocker.patch('time.sleep')
    check_docker.side_effect = [False, False, False, False, True]

    assert check_docker.called is False

    main.main()

    assert check_docker.called is True
    assert check_docker.call_count == 5


def test_check_docker_true(monkeypatch):
    monkeypatch.setattr(docker, 'from_env', lambda: None)
    assert main.check_docker() == True


def test_check_docker_false(monkeypatch):
    def raise_exception():
        raise DockerException()

    monkeypatch.setattr(docker, 'from_env', raise_exception)
    assert main.check_docker() == False
