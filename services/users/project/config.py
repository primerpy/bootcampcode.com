# services/users/project/config.py

import os

from pydantic import Field
from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    TESTING: bool = False
    ENVIRONMENT: str = "dev"
    DATABASE_URL: str | None = None


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    __test__ = False  # Tell pytest this is not a test class

    TESTING: bool = True
    DATABASE_URL: str | None = Field(default=None, validation_alias="DATABASE_TEST_URL")


class ProductionConfig(BaseConfig):
    pass


def get_settings():
    env = os.getenv("ENVIRONMENT", "dev")
    if env == "prod":
        return ProductionConfig()
    elif env == "test":
        return TestingConfig()
    return DevelopmentConfig()
