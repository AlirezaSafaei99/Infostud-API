from fastapi import FastAPI
from app.routes import user
from app.utils.scheduler import scheduler

# Create a single fastAPI application instance
app = FastAPI()

# Include the user-related router
app.include_router(user.router)

# Start the scheduler on the app startup
@app.on_event("startup")
async def startup_event():
    scheduler.start()
