from fastapi import Depends, FastAPI

from project.api.users import router as users_router
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


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(users_router)
    return app


app = create_app()
