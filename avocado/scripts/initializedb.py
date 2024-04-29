import warnings

from sqlalchemy import create_engine
from sqlalchemy import exc

from avocado.config import settings
from avocado.models.main import Cart
from avocado.models.main import Product
from avocado.models.meta import metadata

# Ensure that a warnings filter will not suppress any warnings
warnings.filterwarnings("always", category=exc.Base20DeprecationWarning)


def main():
    SQLALCHEMY_ENGINE_OPTIONS = {
        "echo": True,
        "connect_args": {"connect_timeout": 5},  # seconds
        "future": True,
    }

    engine = create_engine(
        settings.SQLALCHEMY_DATABASE_ASYNC_URI,
        **SQLALCHEMY_ENGINE_OPTIONS,
    )

    with engine.connect() as connection:
        metadata.create_all(
            connection, [model.__table__ for model in [Product, Cart]]
        )
        connection.commit()


if __name__ == "__main__":
    main()
