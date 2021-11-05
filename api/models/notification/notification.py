from api.Exceptions.empty_parameter_error import EmptyParameterError
from api.Constants import NOTIF_BODY, NOTIF_TITLE


class Notification():

    def __init__(self, receiver_expo_token = None):
        if not receiver_expo_token:
            raise EmptyParameterError('receiver_expo_token')
        self.receiver_expo_token = receiver_expo_token
        self.title = NOTIF_BODY
        self.body = NOTIF_TITLE

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_data(self):
        return None
