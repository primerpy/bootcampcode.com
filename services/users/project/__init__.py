from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from project.api.users import router as users_router
from project.config import BaseConfig, configure_logging, get_settings
from project.middleware import TimingMiddleware

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
    settings = get_settings()
    configure_logging(settings)
    app = FastAPI(
        title="BootcampCode",
        description="A microservice for code evaluation",
        version="1.0.0",
        debug=settings.DEBUG,  # new
    )
    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Allows all origins (change for production)
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(TimingMiddleware)
    app.include_router(users_router)
    return app


app = create_app()
