from fastapi import APIRouter
from api.controllers.notification_controller import NotificationController

router = APIRouter(tags=["Notifications"])


@router.get("/notifications/start")
async def start_cron():
    return NotificationController.start_cron()

@router.get("/notifications/stop")
async def stop_cron():
    return NotificationController.stop_cron()

@router.get("/notifications/add")
async def add_jobs():
    return NotificationController.add_job()

@router.get("/notifications/jobs")
async def get_jobs():
    return NotificationController.get_jobs()

@router.post("/notifications/modify/job")
async def modify_jobs(next_run: str = ""):
    return NotificationController.modify_next_run_in_job(next_run)

