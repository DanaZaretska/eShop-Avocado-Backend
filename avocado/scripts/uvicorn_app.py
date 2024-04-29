import uvicorn

from avocado.app.backend.config import settings


def main():
    uvicorn.run(
        settings.APP_BACKEND_IMPORT_STRING,
        host=str(settings.APP_BACKEND_HOST),
        port=int(settings.APP_BACKEND_PORT),
        reload=settings.APP_BACKEND_AUTO_RELOAD,
        workers=settings.APP_BACKEND_WORKERS,
    )


if __name__ == "__main__":
    main()
