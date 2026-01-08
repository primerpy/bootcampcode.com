# services/users/manage.py

import sys
import subprocess
from project.db import Base, engine, SessionLocal
from project.api.models import User


def recreate_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("Database recreated.")


def seed_db():
    db = SessionLocal()
    try:
        user1 = User(username='primerpy', email="primerpy@primerpy.com")
        user2 = User(username='primerpy2', email="primerpy2@primerpy.com")
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


if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "recreate_db":
            recreate_db()
        elif command == "seed_db":
            seed_db()
        elif command == "test":
            test()
        else:
            print(f"Unknown command: {command}")
    else:
        print("Usage: python manage.py [recreate_db|seed_db|test]")
