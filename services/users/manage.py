import sys

from project.db import Base, SessionLocal, engine
from project.api.models immport User


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
        print("Database seeded")
    finally:
        db.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "recreate_db":
            recreate_db()
        elif command == "seed_db":
            seed_db()
        else:
            print(f"Unknown command: {command}")
    else:
        print("Usage: python manage.py [recreate_db|seed_db]")
