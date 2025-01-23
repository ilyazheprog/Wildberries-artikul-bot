from contextlib import asynccontextmanager

from fastapi import FastAPI
from routers import global_router

from modules.scheduler.main import start_scheduler, stop_scheduler

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_scheduler()
    try:
        yield
    finally:
        stop_scheduler()

app = FastAPI(title="WB Scrapper API", lifespan=lifespan)

app.include_router(global_router)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
