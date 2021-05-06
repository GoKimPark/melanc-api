import pytest
import platform


def test_python_version():
    assert platform.python_version() == "3.9.4"

