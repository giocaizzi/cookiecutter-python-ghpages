import pytest
from pathlib import Path


# MARKS


def pytest_configure(config):
    config.addinivalue_line("markers", "wip: WORK IN PROGRESS")


# TEST_ENVIRONMENT

CWD = Path(__file__).resolve()
FIXTURES_ROOT = CWD.parent / "fixtures"
