from fastapi import FastAPI

from project.api.users import router as users_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(users_router)

    return app


app = create_app()
