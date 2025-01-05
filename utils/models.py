# This file defines the SQLAlchemy ORM models for the database.
# Each model represents a table in the database. Here, the User model defines the structure and schema for the "user" table.
# These models are used to perform CRUD operations in the database.

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": "users"}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    info_user = Column(String(100), nullable=False)
    pass_user = Column(String(100), nullable=False)



