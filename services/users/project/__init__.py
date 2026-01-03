from fastapi import FastAPI

from project.config import DevelopmentConfig

app = FastAPI()


settings = DevelopmentConfig()


@app.get("/users/ping")
async def users_ping():
    return {
        "status": "success",
        "message": "pong!",
        "debug": settings.TESTING,
    }
