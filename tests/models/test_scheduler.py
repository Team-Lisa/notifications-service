from api.models.scheduler.scheduler import Scheduler

def tearDown():
    scheduler = Scheduler()
    if scheduler.state == "Started":
        scheduler.stop()

def test_scheduler_is_singleton():
    tearDown()
    first_scheduler = Scheduler()
    if first_scheduler.state == "Started":
        first_scheduler.stop()
    first_scheduler.start()
    first_scheduler.add_job(True)
    second_scheduler = Scheduler()
    second_scheduler.add_job(True)
    assert len(second_scheduler.get_jobs()) == 2
    second_scheduler.stop()

def test_scheduler_stop():
    tearDown()
    scheduler = Scheduler()
    scheduler.start()
    scheduler.stop()
    assert scheduler.state != "Started"
