from fastapi import FastAPI

from project.config import get_settings

app = FastAPI()

settings = get_settings()


@app.get("/users/ping")
async def users_ping():
    return {
        "status": "success",
        "message": "pong!",
        "environment": settings.ENVIRONMENT,
        "testing": settings.TESTING,
    }
