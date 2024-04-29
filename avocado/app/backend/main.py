import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from avocado.app.backend.api import router
from avocado.app.backend.api.errors import global_error_handler
from avocado.app.backend.api.errors import http422_error_handler
from avocado.app.backend.api.errors import http_error_handler
from avocado.app.backend.config import settings


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        version=settings.VERSION,
        docs_url=f"{settings.API_PREFIX}{settings.API_VERSION_PREFIX}/docs",
        redoc_url=f"{settings.API_PREFIX}{settings.API_VERSION_PREFIX}/redoc",
        openapi_url=f"{settings.API_PREFIX}{settings.API_VERSION_PREFIX}/openapi.json",
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(
        RequestValidationError, http422_error_handler
    )
    application.add_exception_handler(Exception, global_error_handler)

    application.include_router(router, prefix=settings.API_PREFIX)

    return application


app = get_application()

if __name__ == "__main__":
    uvicorn.run(
        settings.APP_BACKEND_IMPORT_STRING,
        host=str(settings.APP_BACKEND_HOST),
        port=int(settings.APP_BACKEND_PORT),
        reload=settings.APP_BACKEND_AUTO_RELOAD,
        workers=settings.APP_BACKEND_WORKERS,
    )
