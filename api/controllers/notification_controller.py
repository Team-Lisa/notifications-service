from api.service.scheduler_service import SchedulerService

class NotificationController:

    @staticmethod
    def start_cron():
        message = SchedulerService().start_scheduler()
        return { "message": message}

    @staticmethod
    def add_job():
        message = SchedulerService().add_job_to_scheduler()
        return {"message": message}

    @staticmethod
    def modify_next_run_in_job(date):
        return SchedulerService().modify_jobs(date)

    @staticmethod
    def stop_cron():
        message = SchedulerService().stop_scheduler()
        return {"message": message}

    @staticmethod
    def get_jobs():
        return SchedulerService().get_jobs()
