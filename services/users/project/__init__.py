from fastapi import Depends, FastAPI

from project.config import BaseConfig, get_settings

app = FastAPI()


@app.get("/users/ping")
async def users_ping(settings: BaseConfig = Depends(get_settings)):
    return {
        "status": "success",
        "message": "pong!",
        "environment": settings.ENVIRONMENT,
        "testing": settings.TESTING,
    }
