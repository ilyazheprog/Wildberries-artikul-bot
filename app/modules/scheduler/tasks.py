from sqlalchemy.ext.asyncio import AsyncSession

from modules.database.methods.subscribe import update_subscribe


async def update_subscription_task(artikul: int, session: AsyncSession):
    """Update subscription data periodically."""
    updated = await update_subscribe(session, artikul)
    if not updated:
        print(f"Failed to update subscription for artikul: {artikul}")
