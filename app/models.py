# models.py
# This file defines the SQLAlchemy ORM models for the database.
# Each model represents a table in the database. Here, the User model defines the structure and schema for the "user" table.
# These models are used to perform CRUD operations in the database.

from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": "users"}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    info_user = Column(String(100), nullable=False)
    pass_user = Column(String(100), nullable=False)

class EnrollmentFile(Base):
    __tablename__ = "enrollment file"
    __table_args__ = {"schema": "users"}

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user.id"), nullable=False)
    file_path = Column(String(255), nullable=False)
    pdf_data = Column(LargeBinary, nullable=False)
    uploaded_at = Column(String(50), nullable=False) # Change the type to time
    user = relationship("User", back_populates="enrollment_files")

User.enrollment_files = relationship("EnrollmentFile", back_populates="user")
# do not use the table name directly instead implement a method to get it 
# also for table args 

