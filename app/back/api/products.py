from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from modules.database.methods.products import (
    add_product,
    get_product_by_artikul,
    is_product_exists,
    update_product_by_artikul,
)
from back.schemas import ProductCreate, ProductOut, ProductUpdate, Response
from back.sec import verify_token
from modules.database.connect import get_async_session
from modules.wildberries_api import get_product_details

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("", status_code=201, response_model=ProductOut)
async def create_product(artikul: int, session: AsyncSession = Depends(get_async_session),
                         _: bool = Depends(verify_token)):
    """Create a new product"""
    if await is_product_exists(session, artikul):
        raise HTTPException(status_code=400, detail="Product already exists")
    response = (await get_product_details(artikul))["data"]["products"]
    if not response:
        raise HTTPException(status_code=404, detail="Product not found")
    wb_product = response[0]

    product = ProductCreate(
        artikul=wb_product["id"],
        name=wb_product["name"],
        price_in_copecs=wb_product["salePriceU"],
        rate=wb_product["reviewRating"],
        total_quantity=wb_product["totalQuantity"],
    )

    return await add_product(session, product)

@router.put("/{artikul}", response_model=ProductOut)
async def update_product(
    artikul: int,
    product: ProductUpdate,
    session: AsyncSession = Depends(get_async_session),
    _: bool = Depends(verify_token),
):
    """Update product by artikul"""

    if not await is_product_exists(session, artikul):
        raise HTTPException(status_code=404, detail="Product not found in the database")
    response = (await get_product_details(artikul))["data"]["products"]
    if not response:
        raise HTTPException(status_code=404, detail="Product not found in the Wildberries")
    wb_product = response[0]

    product = ProductCreate(
        artikul=wb_product["id"],
        name=wb_product["name"],
        price_in_copecs=wb_product["salePriceU"],
        rate=wb_product["reviewRating"],
        total_quantity=wb_product["totalQuantity"],
    )

    product = await update_product_by_artikul(session, artikul, **product.dict(exclude_unset=True))
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product