from datetime import datetime, timedelta

from api.models.scheduler.scheduler import Scheduler
from api.Constants import NEXT_RUN, FUNCTION_TO_EXECUTE, SERVICE_STARTED, SERVICE_STOPPED, JOB_ADDED

class SchedulerService:

    def __init__(self):
        self.scheduler = Scheduler()

    def start_scheduler(self):
        self.scheduler.start()
        return SERVICE_STARTED

    def add_job_to_scheduler(self, start_date = None):
        self.scheduler.add_job(start_date=start_date)
        return JOB_ADDED

    def stop_scheduler(self):
        self.scheduler.stop()
        return SERVICE_STOPPED

    def remove_jobs(self):
        return self.scheduler.remove_jobs()

    def get_jobs(self):
        jobs = self.scheduler.get_jobs()
        result = []
        for job in jobs:
            result.append({"Job": [FUNCTION_TO_EXECUTE + job.name, NEXT_RUN + job.next_run_time.strftime('%Y-%m-%d %H:%M:%S')]})
        return result

    def modify_jobs(self, date):
        self.remove_jobs()
        next_run = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
        self.add_job_to_scheduler(next_run)
        jobs = self.scheduler.get_jobs()
        for job in jobs:
            return {"Job": [FUNCTION_TO_EXECUTE + job.name, NEXT_RUN + job.next_run_time.strftime('%Y-%m-%d %H:%M:%S')]}
