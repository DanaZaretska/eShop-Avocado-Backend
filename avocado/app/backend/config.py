from functools import lru_cache
from ipaddress import IPv4Address

from avocado.config import Settings as BaseSettings


class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    API_VERSION_PREFIX: str = "/v1"
    VERSION: str = "0.0.1"
    PROJECT_NAME: str
    ALLOWED_HOSTS: list[str]
    DEBUG: bool = True
    APP_BACKEND_HOST: IPv4Address = "127.0.0.1"
    APP_BACKEND_PORT: int = 8080
    APP_BACKEND_WORKERS: int = 1
    APP_BACKEND_AUTO_RELOAD: bool = False
    APP_BACKEND_IMPORT_STRING: str


@lru_cache
def cached_settings():
    return Settings()


settings = cached_settings()
