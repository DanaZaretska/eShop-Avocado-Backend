import warnings

from sqlalchemy import exc
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from avocado.config import settings

# Ensure that a warnings filter will not suppress any warnings
warnings.filterwarnings("always", category=exc.Base20DeprecationWarning)

SQLALCHEMY_ASYNC_ENGINE_OPTIONS = {
    "echo": True,
    "connect_args": {"connect_timeout": 5},  # seconds
    "future": True,
}

async_engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_ASYNC_URI, **SQLALCHEMY_ASYNC_ENGINE_OPTIONS
)

AsyncSession = async_sessionmaker(
    async_engine, expire_on_commit=False, future=True
)
