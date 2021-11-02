from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta

def Singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@Singleton
class Scheduler():

    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def add_job(self):
        #self.scheduler.add_job(getUsers, 'interval', days=1, start_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.scheduler.add_job(getUsers, 'cron', day_of_week='mon-sun', hour='10-22', start_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def start(self):
        self.add_job()
        self.scheduler.start()

    def stop(self):
        self.scheduler.pause()

    def get_jobs(self):
        self.scheduler.print_jobs()
        return self.scheduler.get_jobs()