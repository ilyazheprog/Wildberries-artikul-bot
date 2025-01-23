from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()


def start_scheduler():
    scheduler.start()


def stop_scheduler():
    scheduler.shutdown(wait=False)


import asyncio


def run_async_task(coroutine_func, *args, **kwargs):
    """Run an async function as a blocking call."""
    asyncio.run(coroutine_func(*args, **kwargs))
