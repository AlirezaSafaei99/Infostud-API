# main.py
# This is the main entry point of the FastAPI application. 
# It initializes the FastAPI app instance and includes routers for different modules.
# It also starts any background tasks, such as the scheduled job, on application startup.

from fastapi import FastAPI
from app.routes import user

# Create a single fastAPI application instance
app = FastAPI()

# Include the user-related router
app.include_router(user.router)


