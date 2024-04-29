from sqlalchemy import BigInteger
from sqlalchemy import Column
from sqlalchemy import ForeignKeyConstraint
from sqlalchemy import Identity
from sqlalchemy import Integer
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import UnicodeText
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from .meta import Base

PUBLIC_SCHEMA = "public"


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, Identity(), nullable=False, index=True)

    title = Column(UnicodeText, nullable=False)
    image = Column(UnicodeText, nullable=False)
    price = Column(BigInteger, nullable=False)
    tags = Column(ARRAY(UnicodeText))

    __table_args__ = (PrimaryKeyConstraint("id"), {"schema": PUBLIC_SCHEMA})


class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, Identity(), nullable=False, index=True)

    product_id = Column(Integer, nullable=False, index=True)

    quantity = Column(BigInteger, nullable=False, server_default=text("1"))

    product = relationship("Product")

    __table_args__ = (
        PrimaryKeyConstraint("id"),
        ForeignKeyConstraint((product_id,), (Product.id,)),
        {"schema": PUBLIC_SCHEMA},
    )
