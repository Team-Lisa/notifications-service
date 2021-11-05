from api.models.notification.notification import Notification
import pytest
from api.Exceptions.empty_parameter_error import EmptyParameterError

def test_notification_empty_receiver_expo_token():
    with pytest.raises(EmptyParameterError):
        Notification(None)