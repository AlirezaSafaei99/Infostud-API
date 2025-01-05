from fastapi import FastAPI
from routes import user
import uvicorn

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

# Include the user router
app.include_router(user.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
