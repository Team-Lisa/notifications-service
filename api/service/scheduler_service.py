from datetime import datetime, timedelta

from api.models.scheduler.scheduler import Scheduler
from api.Constants import NEXT_RUN, FUNCTION_TO_EXECUTE, SERVICE_STARTED, SERVICE_STOPPED, JOB_ADDED

class SchedulerService:

    def __init__(self):
        self.scheduler = Scheduler()

    def start_scheduler(self):
        self.scheduler.start()
        return SERVICE_STARTED

    def add_job_to_scheduler(self):
        self.scheduler.add_job()
        return JOB_ADDED

    def stop_scheduler(self):
        self.scheduler.stop()
        return SERVICE_STOPPED

    def get_jobs(self):
        jobs = self.scheduler.get_jobs()
        result = []
        for job in jobs:
            result.append({"Job": [FUNCTION_TO_EXECUTE + job.name, NEXT_RUN + job.next_run_time.strftime('%Y/%m/%d %H:%M:%S')]})
        return result

    def modify_jobs(self, date):
        next_run = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        jobs = self.scheduler.get_jobs()
        for job in jobs:
            job.modify(next_run_time=next_run)
            return {"Job": [FUNCTION_TO_EXECUTE + job.name, NEXT_RUN + job.next_run_time.strftime('%Y/%m/%d %H:%M:%S')]}
