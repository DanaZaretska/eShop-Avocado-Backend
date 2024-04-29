from sqlalchemy import delete
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from avocado.models.main import Cart

from . import BaseService

LIST_LIMIT_DEFAULT = 10


class CartService(BaseService):
    async def view(self):
        s = (
            select(Cart)
            .options(selectinload(Cart.product))
            .order_by(Cart.id.desc())
        )

        result = await self.dbsession.execute(s)

        return result.scalars().all()

    async def item_add(self, *, product_id: int):
        s = select(Cart).where(Cart.product_id == product_id)
        result = await self.dbsession.execute(s)

        if result.scalars().first() is not None:
            return

        item = Cart(product_id=product_id)
        self.dbsession.add(item)

        await self.dbsession.commit()

    async def item_remove(self, *, item_id: int):
        s = delete(Cart).where(Cart.id == item_id)

        await self.dbsession.execute(s)
        await self.dbsession.commit()

    async def item_increment(self, *, item_id: int):
        s = select(Cart).where(Cart.id == item_id)

        result = await self.dbsession.execute(s)
        item = result.scalars().first()

        if item is not None:
            item.quantity += 1
            await self.dbsession.commit()

    async def item_decrement(self, *, item_id: int):
        s = select(Cart).where(Cart.id == item_id)

        result = await self.dbsession.execute(s)
        item = result.scalars().first()

        if item is not None and item.quantity > 1:
            item.quantity -= 1
            await self.dbsession.commit()

    async def clear(self):
        s = delete(Cart)

        await self.dbsession.execute(s)
        await self.dbsession.commit()
