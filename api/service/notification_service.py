from api.models.notification.notification import Notification
from api.service.notification_sender import NotificationSender
from api.Constants import USER_SERVICE
import requests

class NotificationService:

    def __init__(self):
        self.sender = NotificationSender()

    def send_notifications(self):
        self.send_notif_users_first_five_days()
        self.send_notif_users_more_one_week()
        self.send_notif_users_more_two_months()

    def send_notif_users_first_five_days(self):
        users = self.get_users(5,0)['users']
        self.send_notifications_to_users(users)

    def send_notif_users_more_one_week(self):
        users = self.get_users(59, 7)['users']
        self.send_notifications_to_users(users)

    def send_notif_users_more_two_months(self):
        users = self.get_users(-1, 60)['users']
        self.send_notifications_to_users(users)

    def send_notifications_to_users(self, users):
        for user in users:
            notification = Notification(user['expo_token'])
            self.sender.send_notification(notification)

    def get_users(self, frm, to):
        payload = {'frm': str(frm), 'to': str(to)}
        users = requests.get(USER_SERVICE, params=payload)
        return users.json()
