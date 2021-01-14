import time
from threading import Lock, Thread

from main import AlertManager


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


def test_multi_thread_input():
    messages = ['message1', 'message2', 'message1']
    lock = Lock()
    x = 0

    def alert_generator(idx, sleep_time):
        nonlocal x
        p = AlertManager.getInstance()
        t = 0
        while t < 60:
            t += sleep_time
            if p.send_alert(messages[idx]):
                with lock:
                    x += 1
            time.sleep(sleep_time)

    t = [4, 10, 3]
    threads = [Thread(target=alert_generator, args=(i, t[i])) for i in range(len(t))]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(x)
    assert x == 16
