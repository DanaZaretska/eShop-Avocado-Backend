from pydantic import BaseModel

from .product import ProductResponseSchema


class CartResponseSchema(BaseModel):
    id: int
    product_id: int
    quantity: int | None = 1
    product: ProductResponseSchema | None

    class Config:
        orm_mode = True
