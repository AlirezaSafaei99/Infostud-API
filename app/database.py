# THIS FILE IS RESPONSIBLE TO GET CONNECTED TO THE DB SO  WE WILL HAVE THE AUTHORIZATION TO MODIFY STUFF ON DB.
from config.config import load_config
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

def init_db():
    config = load_config()
    SQLALCHEMY_DATABASE_URL = config['database']['APP_DB_DNS']

    # Make sure to use asyncpg driver for async support
    engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

    async_session = sessionmaker(
        engine,
        class_=AsyncSession,  # Use AsyncSession to manage async sessions
        expire_on_commit=False,  # Prevent sessions from expiring on commit
    )

    return async_session