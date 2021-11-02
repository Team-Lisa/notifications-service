from api.service.notification_service import NotificationService

class NotificationController:

    @staticmethod
    def start_cron():
        return NotificationService().start_scheduler()

    @staticmethod
    def stop_cron():
        return NotificationService().start_scheduler()

    @staticmethod
    def get_jobs():
        return NotificationService().get_jobs()
