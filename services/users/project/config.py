# services/users/project/config.py

import logging
import os

from pydantic import Field
from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    TESTING: bool = False
    ENVIRONMENT: str = "dev"
    DATABASE_URL: str | None = None


class DevelopmentConfig(BaseConfig):
    ENVIRONMENT: str = "dev"
    LOG_LEVEL: str = "DEBUG"
    DEBUG: bool = True


class TestingConfig(BaseConfig):
    __test__ = False  # Tell pytest this is not a test class

    TESTING: bool = True
    DATABASE_URL: str | None = Field(default=None, validation_alias="DATABASE_TEST_URL")


class ProductionConfig(BaseConfig):
    ENVIRONMENT: str = "prod"
    LOG_LEVEL: str = "DEBUG"
    DEBUG: bool = True


def get_settings():
    env = os.getenv("ENVIRONMENT", "dev")
    if env == "prod":
        return ProductionConfig()
    elif env == "test":
        return TestingConfig()
    return DevelopmentConfig()


def configure_logging(settings: BaseConfig):
    logging.basicConfig(
        level=getattr(logging, settings.LOG_LEVEL),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.engine").setLevel(
        logging.DEBUG if settings.DEBUG else logging.WARNING
    )
