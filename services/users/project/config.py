# services/users/project/config.py

import os

from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    TESTING: bool = False
    ENVIRONMENT: str = "dev"


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING: bool = True


class ProductionConfig(BaseConfig):
    pass


def get_settings():
    env = os.getenv("ENVIRONMENT", "dev")
    if env == "prod":
        return ProductionConfig()
    elif env == "test":
        return TestingConfig()
    return DevelopmentConfig()
