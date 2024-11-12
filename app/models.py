# Database models (User model)
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


# do not use the table name directly instead implement a method to get it 
# also for table args 

