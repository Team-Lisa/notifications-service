from api.service.notification_service import NotificationService

class NotificationController:

    @staticmethod
    def start_cron():
        message = NotificationService().start_scheduler()
        return { "message": message}

    @staticmethod
    def stop_cron():
        message = NotificationService().stop_scheduler()
        return {"message": message}

    @staticmethod
    def get_jobs():
        return NotificationService().get_jobs()
