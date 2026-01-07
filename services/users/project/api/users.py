from fastapi import APIRouter

from project.config import get_settings

router = APIRouter()
settings = get_settings()


@router.get("/users/ping")
async def users_ping():
    return {
        "status":"success",
        "message":"pong!",
        "environment": settings.ENVIRONMENT,
        "testing":settings.TESTING
    }
