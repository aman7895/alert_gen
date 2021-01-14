from main import AlertManager
import time


def test_one_message_multiple_calls():
    alerts = AlertManager.getInstance()
    x = 0
    for i in range(10):
        x += 1 if alerts.send_alert("This should print twice") else 0
        time.sleep(1)
    assert x == 2


def test_cannot_create_instance_of_alert_manager():
    is_error_thrown = False
    try:
        AlertManager()
    except:
        is_error_thrown = True
    assert is_error_thrown
