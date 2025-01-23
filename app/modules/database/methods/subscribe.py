from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from modules.database.methods.products import is_product_exists

from ..models import Subscribe

async def add_subscribe(
    session: AsyncSession,
    artikul: int,
) -> Subscribe:
    """Add a new subscribe to the database"""
    if not await is_product_exists(session, artikul):
        return False
    subscribe = Subscribe(artikul=artikul)
    session.add(subscribe)
    await session.commit()
    return True

async def get_subscribe_by_artikul(
    session: AsyncSession,
    artikul: int,
) -> Subscribe:
    """Get subscribe by artikul"""
    stmt = select(Subscribe).where(Subscribe.artikul == artikul)
    result = await session.execute(stmt)
    return result.scalars().first()

async def update_subscribe(
    session: AsyncSession,
    artikul: int,
) -> datetime:
    """Update subscribe by artikul"""
    subscribe = await get_subscribe_by_artikul(session, artikul)
    if not subscribe:
        return False
    subscribe.last_update = datetime.now()
    await session.commit()
    return subscribe.last_update

async def is_subscribe_exists(
    session: AsyncSession,
    artikul: int,
) -> bool:
    """Check if subscribe exists"""
    subscribe = await get_subscribe_by_artikul(session, artikul)
    return subscribe is not None

__all__ = ["add_subscribe", "get_subscribe_by_artikul", "update_subscribe", 
           "is_subscribe_exists"]