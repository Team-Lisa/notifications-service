import pytest
from api.controllers.notification_controller import NotificationController

def test_start(init):
    response = NotificationController.start_cron()
    assert response == {
        "The notifications service has started."
    }


def test_stop(init):
    response = NotificationController.stop_cron()
    assert response == {
        "The notifications service has stopped."
    }
