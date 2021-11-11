from datetime import datetime, timedelta
from api.models.notification.notification import Notification
from api.service.notification_sender import NotificationSender
from api.Constants import USER_SERVICE
import requests


def calculate_next_notification_date(case, days_since_last_connection):
    today = datetime.now().date()
    if case == 1:
        if days_since_last_connection == 5:
            next_notification = today + timedelta(days=2)
        else:
            next_notification = today + timedelta(days=1)
    elif case == 2:
        next_notification = today + timedelta(days=7)
    else:
        next_notification = today + timedelta(days=30)
    return next_notification.strftime('%Y-%m-%d')

def get_users(frm, to):
    payload = {'frm': str(frm), 'to': str(to)}
    users = requests.get(USER_SERVICE + "lastConnection", params=payload)
    return users.json()


def update_user(next_notification, user):
    requests.patch(USER_SERVICE + "nextNotification", data ={'next_notification_date':next_notification, 'email': user['email']})


class NotificationService:

    def __init__(self):
        self.sender = NotificationSender()

    def send_notifications(self):
        self.send_notif_users_first_five_days()
        self.send_notif_users_more_one_week()
        self.send_notif_users_more_two_months()

    def send_notif_users_first_five_days(self):
        users = get_users(5,0)['users']
        self.send_notifications_to_users(users, 1)

    def send_notif_users_more_one_week(self):
        users = get_users(59, 7)['users']
        self.send_notifications_to_users(users, 2)

    def send_notif_users_more_two_months(self):
        users = get_users(-1, 60)['users']
        self.send_notifications_to_users(users, 3)

    def send_notifications_to_users(self, users, case):
        today = datetime.now().date()
        today_with_time = datetime(year=today.year, month=today.month, day=today.day)
        for user in users:
            user_last_connection = datetime.strptime(user['last_connection'], '%Y-%m-%d')
            days_since_last_connection = today_with_time - user_last_connection
            if user['next_notification'] == today.strftime('%Y-%m-%d'):
                if user['expo_token'] == None: continue
                notification = Notification(user['expo_token'])
                self.sender.send_notification(notification)
                next_notification = calculate_next_notification_date(case, days_since_last_connection)
                update_user(next_notification, user)
