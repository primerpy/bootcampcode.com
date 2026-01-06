import os

from project.config import (
    DevelopmentConfig,
    ProductionConfig,
    TestingConfig,
    get_settings,
)


def test_development_config(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "dev")
    settings = get_settings()
    assert settings.TESTING is False
    assert isinstance(settings, DevelopmentConfig)
    assert os.environ.get("DATABASE_URL") == settings.DATABASE_URL


def test_testing_config(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "test")
    settings = get_settings()
    assert settings.TESTING is True
    assert isinstance(settings, TestingConfig)
    assert os.environ.get("DATABASE_TEST_URL") == settings.DATABASE_URL


def test_production_config(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "prod")
    settings = get_settings()
    assert settings.TESTING is False
    assert isinstance(settings, ProductionConfig)
    assert os.environ.get("DATABASE_URL") == settings.DATABASE_URL
