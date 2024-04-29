from sqlalchemy.future import select

from avocado.models.main import Product

from . import BaseService

LIST_LIMIT_DEFAULT = 10


class ProductService(BaseService):
    async def list(
        self,
        *,
        limit: int | None = LIST_LIMIT_DEFAULT,
        offset: int | None = None,
    ):
        s = select(Product).limit(limit).offset(offset)

        result = await self.dbsession.execute(s)

        return result.scalars().all()

    async def view(self, *, product_id: int):
        s = select(Product).where(Product.id == product_id)

        result = await self.dbsession.execute(s)

        return result.scalars().first()
