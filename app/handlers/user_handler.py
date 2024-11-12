from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import User

async def create_user(db: AsyncSession, user_data):
    user = User(**user_data)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def get_user_by_id(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalar_one_or_none()

async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()

async def update_user(db: AsyncSession, user_id: int, updated_data):
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalar_one_or_none()
    if user:
        for key, value in updated_data.items():
            setattr(user, key, value)
        await db.commit()
        await db.refresh(user)
    return user

async def delete_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalar_one_or_none()
    if user:
        await db.delete(user)
        await db.commit()
    return user