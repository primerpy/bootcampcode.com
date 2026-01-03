from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    """Base configuration"""

    TESTING: bool = False


class DevelopmentConfig(BaseConfig):
    """Development configuration"""

    pass


class TestingConfig(BaseConfig):
    """Testing configuration"""

    TESTING: bool = True


class ProductionConfig(BaseConfig):
    """Production configuration"""

    pass
