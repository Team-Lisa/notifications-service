from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushServerError,
)

class NotificationSender():
    def send_notification(self, notification):
        # Basic arguments. You should extend this function with the push features you
        # want to use, or simply pass in a `PushMessage` object.
        response = PushClient().publish(
            PushMessage(to=notification.receiver_expo_token,
                        title=notification.get_title(),
                        body=notification.get_body(),
                        display_in_foreground=True,
                        sound='default',
                        data=notification.get_data()))
        # We got a response back, but we don't know whether it's an error yet.
        # This call raises errors so we can handle them with normal exception
        # flows.
        response.validate_response()
