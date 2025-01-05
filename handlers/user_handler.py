# user_handler.py
# This file contains the core logic for handling user operations in the database.
# It defines functions for creating, retrieving, updating, and deleting user records in an asynchronous manner.
# These functions interact with the database via SQLAlchemy and are called by the API routes.

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from utils.models import User

async def create_user(db: AsyncSession, user_data):
    user = User(**user_data)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def get_user_by_id(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalars().first()

async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()

async def update_user(db: AsyncSession, user_id: int, updated_data):
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalars().first()
    if user:
        for key, value in updated_data.items():
            setattr(user, key, value)
        await db.commit()
        await db.refresh(user)
    return user

async def delete_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalars().first()
    if user:
        await db.delete(user)
        await db.commit()
    return user
