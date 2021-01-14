from main import AlertManager
import time


def test_one_message_multiple_calls():
    alerts = AlertManager.getInstance()
    x = 0
    for i in range(10):
        x += 1 if alerts.send_alert("This should print twice") else 0
        time.sleep(1)
    assert x == 2