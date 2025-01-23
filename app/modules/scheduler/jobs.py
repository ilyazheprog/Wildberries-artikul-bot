from sqlalchemy.ext.asyncio import AsyncSession
from apscheduler.triggers.interval import IntervalTrigger
from modules.scheduler.tasks import update_subscription_task
from modules.scheduler.main import run_async_task, scheduler

def job_schedule_subscription_task(artikul: int, session: AssertionError, minutes: int = 30):
    """Schedule periodic subscription updates."""
    scheduler.add_job(
        run_async_task,
        args=[update_subscription_task, artikul, session],
        trigger=IntervalTrigger(minutes=minutes),
        id=str(artikul),
        replace_existing=True
    )
