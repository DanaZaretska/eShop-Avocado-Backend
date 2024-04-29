from fastapi import APIRouter
from fastapi import Depends

from avocado.app.backend.api.dependencies.common import get_service
from avocado.app.backend.schemas.product import ProductResponseSchema
from avocado.app.backend.services.product import ProductService

router = APIRouter()


@router.post(
    "/list", response_model=list[ProductResponseSchema], name="product:list"
)
async def product_list(
    product: ProductService = Depends(get_service(ProductService)),
):
    data = await product.list(limit=10, offset=0)

    return data


@router.post(
    "/view/{product_id}",
    response_model=ProductResponseSchema,
    name="product:view",
)
async def product_view(
    product_id: int,
    product: ProductService = Depends(get_service(ProductService)),
):
    data = await product.view(product_id=product_id)

    return data
