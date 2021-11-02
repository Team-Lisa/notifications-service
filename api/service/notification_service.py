from api.models.scheduler.scheduler import Scheduler

class NotificationService:

    def __init__(self):
        self.scheduler = Scheduler()

    def start_scheduler(self):
        self.scheduler.start()
        return "The notifications service has started."

    def stop_cron(self):
        self.scheduler.stop()
        return "The notifications service has stopped."

    def get_jobs(self):
        jobs = self.scheduler.get_jobs()
        result = []
        for job in jobs:
            print(job)
            result.append({"Job": ["function to execute: " + job.name, "next run at " + job.next_run_time.strftime('%Y/%m/%d %H:%M:%S')]})
        return result