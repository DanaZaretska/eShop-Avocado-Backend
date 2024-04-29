from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

metadata = MetaData()
BaseDeclarative = declarative_base(metadata=metadata)


class Base(BaseDeclarative):
    __abstract__ = True

    __mapper_args__ = {"eager_defaults": True}
