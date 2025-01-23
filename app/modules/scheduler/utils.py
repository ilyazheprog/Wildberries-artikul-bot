from .main import scheduler

def is_task_exists(task_id: str) -> bool:
    """Check if the task exists in the scheduler."""
    return scheduler.get_job(task_id) is not None