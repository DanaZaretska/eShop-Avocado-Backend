from pydantic import BaseModel


class ProductResponseSchema(BaseModel):
    id: int
    title: str
    image: str
    price: int
    tags: list[str]

    class Config:
        orm_mode = True
