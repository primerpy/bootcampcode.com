# services/users/project/tests/conftest.py

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from project import app
from project.api.models import User
from project.config import TestingConfig, get_settings
from project.db import Base, get_db

# Create test engine and session
test_settings = TestingConfig()
test_engine = create_engine(test_settings.DATABASE_URL)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


def get_settings_override():
    return test_settings


@pytest.fixture(scope="module")
def session():
    """Create a fresh database for each test module."""
    # Create all tables
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)

    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def test_app(session):
    """Create a test client with dependency overrides."""

    def get_db_override():
        return session

    # Override both get_db and get_settings
    app.dependency_overrides[get_db] = get_db_override
    app.dependency_overrides[get_settings] = get_settings_override

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def empty_db(session):
    """Clear all users from the database for tests that need empty state."""
    session.query(User).delete()
    session.commit()
    yield session


def add_user(username: str, email: str) -> User:
    """Helper function to add a user directly to the test database."""
    db = TestSessionLocal()
    try:
        user = User(username=username, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    finally:
        db.close()
