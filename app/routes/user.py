# user.py
# This file defines the API endpoints (routes) for user-related operations.
# It includes routes for creating, retrieving, updating, and deleting user data.
# All routes in this file are managed under an APIRouter instance for modularity and ease of inclusion in the main app.

import logging
from fastapi import APIRouter, Depends, HTTPException, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import UserBase
from app.handlers.user_handler import create_user, get_user_by_id, get_users, update_user, delete_user
from app.database import init_db

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)  # Logs INFO level and above

# Dependency that provides the database session
async def get_db() -> AsyncSession: # type: ignore
    logger.info("Getting database session")
    async with init_db()() as session:  # This returns a session object
        yield session
    logger.info("Database session closed")

router = APIRouter()

@router.get("/ping")
def read_root():
    logger.info("Ping received, sending pong response")
    return {"message": "pong"}

@router.post("/users", response_model=UserBase, summary="Create a new user", description="Creates a new user with the provided data.")
async def api_create_user(user_data: dict, db: AsyncSession = Depends(get_db)):
    logger.info("Creating new user with data: %s", user_data)
    user = await create_user(db, user_data)
    logger.info("User created successfully: %s", user)
    return user

@router.get("/user/{user_id}", response_model=UserBase, summary="Get user by ID", description="Fetches a user by their unique ID.")
async def api_get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):
    logger.info("Fetching user with ID: %d", user_id)
    user = await get_user_by_id(db, user_id)
    if not user:
        logger.warning("User with ID %d not found", user_id)
        raise HTTPException(status_code=404, detail="User not found")
    logger.info("User fetched successfully: %s", user)
    return user

@router.get("/users", response_model=list[UserBase], summary="Get all users", description="Fetches all users from the database.")
async def api_get_users(db: AsyncSession = Depends(get_db)):
    logger.info("Fetching all users")
    users = await get_users(db)
    logger.info("Users fetched successfully: %d users", len(users))
    return users

@router.put("/users/:user_id", response_model=UserBase, summary="Update a user", description="Updates user details by their ID.")
async def api_update_user(user_id: int, updated_data: dict, db: AsyncSession = Depends(get_db)):
    logger.info("Updating user with ID %d using data: %s", user_id, updated_data)
    user = await update_user(db, user_id, updated_data)
    if not user:
        logger.warning("User with ID %d not found for update", user_id)
        raise HTTPException(status_code=404, detail="User not found")
    logger.info("User updated successfully: %s", user)
    return user

@router.delete("/delete-users/{user_id}", response_model=UserBase, summary="Delete a user", description="Deletes a user by their ID.")
async def api_delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    logger.info("Deleting user with ID: %d", user_id)
    user = await delete_user(db, user_id)
    if not user:
        logger.warning("User with ID %d not found for deletion", user_id)
        raise HTTPException(status_code=404, detail="User not found")
    logger.info("User deleted successfully: %s", user)
    return user
