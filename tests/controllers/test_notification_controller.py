import pytest
from api.controllers.notification_controller import NotificationController
from api.Constants import SERVICE_STARTED, JOB_ADDED, SERVICE_STOPPED
from unittest.mock import MagicMock


def test_start(init):
    notifictaion_controller = NotificationController()
    notifictaion_controller.start_cron = MagicMock(return_value=SERVICE_STARTED)
    response = NotificationController.start_cron()
    assert response == {
        "message": "The notifications service has started."
    }

def test_add_job(init):
    notifictaion_controller = NotificationController()
    notifictaion_controller.add_job = MagicMock(return_value=JOB_ADDED)
    response = NotificationController.add_job()
    assert response == {
        "message": "The job was added to the scheduler."
    }

def test_stop(init):
    notifictaion_controller = NotificationController()
    notifictaion_controller.stop_cron = MagicMock(return_value=SERVICE_STOPPED)
    response = NotificationController.stop_cron()
    assert response == {
        "message": "The notifications service has stopped."
    }

def test_get_jobs(init):
    notifictaion_controller = NotificationController()
    notifictaion_controller.get_jobs = MagicMock(return_value=[{"Job": ["function to execute: Dummy", "next run at 2021-05-20"]}])
    response = notifictaion_controller.get_jobs()
    assert len(response) == 1
    assert (response[0]['Job'][0]).__contains__("function to execute:")
    assert (response[0]['Job'][1]).__contains__("next run at")

