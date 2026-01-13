# services/users/manage.py

import subprocess
import sys

from project.api.models import User
from project.db import Base, SessionLocal, engine


def recreate_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("Database recreated.")


def seed_db():
    db = SessionLocal()
    try:
        user1 = User(username="primerpy", email="primerpy@primerpy.com")
        user2 = User(username="primerpy2", email="primerpy2@primerpy.com")
        db.add(user1)
        db.add(user2)
        db.commit()
        print("Database seeded.")
    finally:
        db.close()


def test():
    """Runs the tests with pytest."""
    result = subprocess.run(["pytest", "-v"], cwd="/usr/src/app")
    sys.exit(result.returncode)


def cov():
    """
    Run pytest with coverage
    """
    result = subprocess.run(
        ["pytest", "--cov=project", "--cov-report=term-missing", "--cov-report=html"],
        capture_output=False,
    )
    sys.exit(result.returncode)


def lint():
    """
    Run ruff linter
    """
    result = subprocess.run(["ruff", "check", "project"], capture_output=False)
    sys.exit(result.returncode)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "recreate_db":
            recreate_db()
        elif command == "seed_db":
            seed_db()
        elif command == "test":
            test()
        elif command == "cov":
            cov()
        elif command == "lint":
            lint()
        else:
            print(f"Unknown command: {command}")
    else:
        print("Usage: python manage.py [recreate_db|seed_db|test]")
