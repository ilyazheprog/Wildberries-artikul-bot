from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from ..models import Product
from back.schemas import ProductCreate

async def add_product(
    session: AsyncSession,
    product: ProductCreate,
) -> Product:
    """Add a new product to the database"""
    product = Product(**product.model_dump())
    session.add(product)
    await session.commit()
    return product


async def get_product_by_artikul(session: AsyncSession, artikul: int) -> Product:
    """Get product by artikul"""
    stmt = select(Product).where(Product.artikul == artikul)
    result = await session.execute(stmt)
    return result.scalars().first()

async def is_product_exists(session: AsyncSession, artikul: int) -> bool:
    """Check if product exists"""
    product = await get_product_by_artikul(session, artikul)
    return product is not None


async def update_product_by_artikul(
    session: AsyncSession,
    artikul: int,
    name: str = None,
    price_in_copecs: int = None,
    rate: float = None,
    total_quantity: int = None,
) -> Product:
    """Update product by artikul"""
    product = await get_product_by_artikul(session, artikul)

    if not product:
        return None
    if name:
        product.name = name
    if price_in_copecs:
        product.price_in_copecs = price_in_copecs
    if rate:
        product.rate = rate
    if total_quantity:
        product.total_quantity = total_quantity
    await session.commit()
    return product


__all__ = ["add_product", "get_product_by_artikul", 
           "is_product_exists",
           "update_product_by_artikul"]
