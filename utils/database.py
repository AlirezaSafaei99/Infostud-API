# This file is responsible for setting up and managing the database connection.
# It initializes an asynchronous SQLAlchemy database engine and provides an async session factory.
# The session factory is used to create session instances that manage transactions and queries with the database.

from config.config import load_config
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

def init_db():
    config = load_config()
    SQLALCHEMY_DATABASE_URL = config['database']['APP_DB_DNS']

    engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

    async_session = sessionmaker(
        engine,
        class_=AsyncSession,  
        expire_on_commit=False,  
    )

    return async_session