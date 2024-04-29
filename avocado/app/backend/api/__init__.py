from fastapi import APIRouter

from avocado.app.backend.config import settings

from .endpoints import cart
from .endpoints import product

router = APIRouter(prefix=settings.API_VERSION_PREFIX)
router.include_router(product.router, tags=["product"], prefix="/product")
router.include_router(cart.router, tags=["cart"], prefix="/cart")
