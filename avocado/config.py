import os
from typing import Any
from typing import Literal

from pydantic import AnyUrl
from pydantic import BaseSettings
from pydantic import validator


class PostgresDsn(AnyUrl):
    allowed_schemes = {"postgresql+psycopg"}

    user_required = True


def _assemble_db_connection(
    v: str | None,
    values: dict[str, Any],
    driver: Literal["psycopg"] = "psycopg",
) -> Any:
    if isinstance(v, str):
        return v

    return PostgresDsn.build(
        scheme=f"postgresql+{driver}",
        user=values.get("POSTGRES_USER"),
        password=values.get("POSTGRES_PASSWORD"),
        host=values.get("POSTGRES_SERVER"),
        port=str(values.get("POSTGRES_PORT")),
        path=f'/{values.get("POSTGRES_DB")}',
    )


class Settings(BaseSettings):
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    SQLALCHEMY_DATABASE_ASYNC_URI: PostgresDsn | None = None

    @validator("SQLALCHEMY_DATABASE_ASYNC_URI", pre=True)
    def assemble_db_connection_async(
        cls, v: str | None, values: dict[str, Any]
    ) -> Any:
        # calling create_async_engine() with postgresql+psycopg://... will automatically select the async version
        return _assemble_db_connection(v, values, driver="psycopg")

    class Config:
        env_file = os.getenv("AVOCADO_ENV")
        env_file_encoding = "utf-8"


settings = Settings()
