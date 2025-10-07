from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


def create_app() -> FastAPI:
    app = FastAPI(
        title='fastapi-app',
        redoc_url=None,
        default_response_class=ORJSONResponse,
        swagger_ui_parameters={'defaultModelsExpandDepth': -1},
    )

    return app
