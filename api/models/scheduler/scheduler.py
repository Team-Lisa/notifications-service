from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from api.service.notification_service import NotificationService

def Singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

def send_notifications(test = False):
    if test:
        return
    NotificationService().send_notifications()
    return

@Singleton
class Scheduler():

    def __init__(self):
        self.state = None
        self.scheduler = BackgroundScheduler()

    def add_job(self, test = False):
        yesterday = datetime.now() - timedelta(hours=23.9)
        self.scheduler.add_job(send_notifications, 'interval', args = [test], days=1, start_date=yesterday.strftime("%Y-%m-%d %H:%M:%S"))

    def start(self):
        if self.state == "Started":
            return "Scheduler already running"
        self.scheduler.start()
        self.state = "Started"

    def stop(self):
        self.scheduler.shutdown(False)
        self.state = "Stopped"

    def get_jobs(self):
        self.scheduler.print_jobs()
        return self.scheduler.get_jobs()
