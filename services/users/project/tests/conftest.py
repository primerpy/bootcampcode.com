import os

import pytest
from fastapi.testclient import TestClient

from project import app
from project.config import TestingConfig, get_settings


def get_settings_override():
    return TestingConfig()


@pytest.fixture(scope="module")
def test_app():
    # 1. Set up
    # We explicitly set the environment to ensure consistency
    os.environ["ENVIRONMENT"] = "test"
    app.dependency_overrides[get_settings] = get_settings_override

    with TestClient(app) as client:
        yield client  # testing happens here

    # 2. Tear down
    app.dependency_overrides.clear()
