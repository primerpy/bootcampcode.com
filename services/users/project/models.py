from sqlalchemy import Boolean, Column, Integer, String

from project.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    active = Column(Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
