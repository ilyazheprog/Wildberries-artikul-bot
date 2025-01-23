from contextlib import asynccontextmanager

from fastapi import FastAPI
from modules.envs.settings import settings
from modules.scheduler.jobs import job_schedule_subscription_task
from routers import global_router

from modules.scheduler.main import start_scheduler, stop_scheduler
from modules.database.connect import async_session
from modules.database.methods.subscribe import get_artikles_subscribed

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_scheduler()
    try:
        async with async_session() as session:
            for artikul in await get_artikles_subscribed(session):
                job_schedule_subscription_task(
                    artikul, session, settings.wildberries.minutes_to_update_subscriptions
                )
        yield
    finally:
        stop_scheduler()


app = FastAPI(title="WB Scrapper API", lifespan=lifespan)

app.include_router(global_router)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
