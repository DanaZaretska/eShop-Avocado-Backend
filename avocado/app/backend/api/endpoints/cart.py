from fastapi import APIRouter
from fastapi import Depends

from avocado.app.backend.api.dependencies.common import get_service
from avocado.app.backend.schemas.cart import CartResponseSchema
from avocado.app.backend.services.cart import CartService

router = APIRouter()


@router.post(
    "/view", response_model=list[CartResponseSchema], name="cart:view"
)
async def cart_list(cart: CartService = Depends(get_service(CartService))):
    data = await cart.view()

    return data


@router.post("/view", name="cart:clear")
async def cart_clear(cart: CartService = Depends(get_service(CartService))):
    await cart.clear()


@router.post("/item/{product_id}/add", name="cart:item:add")
async def cart_item_add(
    product_id: int, cart: CartService = Depends(get_service(CartService))
):
    await cart.item_add(product_id=product_id)


@router.post("/item/{item_id}/remove", name="cart:item:remove")
async def cart_item_remove(
    item_id: int, cart: CartService = Depends(get_service(CartService))
):
    await cart.item_remove(item_id=item_id)


@router.post("/item/{item_id}/increment", name="cart:item:increment")
async def cart_item_increment(
    item_id: int, cart: CartService = Depends(get_service(CartService))
):
    await cart.item_increment(item_id=item_id)


@router.post("/item/{item_id}/decrement", name="cart:item:decrement")
async def cart_item_decrement(
    item_id: int, cart: CartService = Depends(get_service(CartService))
):
    await cart.item_decrement(item_id=item_id)
