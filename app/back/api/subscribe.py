from apscheduler.triggers.interval import IntervalTrigger
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from modules.scheduler.utils import is_task_exists
from modules.envs.settings import settings
from modules.scheduler.jobs import job_schedule_subscription_task
from modules.scheduler.tasks import update_subscription_task
from modules.database.methods.subscribe import (
    add_subscribe,
    get_subscribe_by_artikul,
    update_subscribe,
    is_subscribe_exists
)
from back.schemas import ProductCreate, ProductOut, ProductUpdate, Response
from modules.database.connect import get_async_session
from modules.wildberries_api import get_product_details
from back.sec import verify_token

router = APIRouter(prefix="/subscribe", tags=["Subscribe"])

@router.get("/{artikul}", response_model=Response)
async def subscribe(artikul: int, session: AsyncSession = Depends(get_async_session),
                    _: bool = Depends(verify_token)):
    """Subscribe to product and schedule periodic updates"""
    if await is_subscribe_exists(session, artikul):
        raise HTTPException(status_code=400, detail="Already subscribed")
    
    if not await add_subscribe(session, artikul):
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Schedule periodic task
    if not is_task_exists(str(artikul)):
        job_schedule_subscription_task(artikul, session, settings.wildberries.minutes_to_update_subscriptions)

    return Response(message="Subscribed and periodic updates scheduled")


@router.put("/{artikul}", response_model=Response)
async def update_subscribe_router(artikul: int, session: AsyncSession = Depends(get_async_session),
                                  _: bool = Depends(verify_token)):
    """Update subscribe by artikul"""
    updated = await update_subscribe(session, artikul)
    if not updated:
        raise HTTPException(status_code=404, detail="Subscribe not found")
    return Response(message="Subscribe updated")