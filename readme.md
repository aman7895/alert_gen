## alert_gen

### Description:
- `config.py` has the `wait_time` config where the alert message waiting time can be configured
- `main.py` defines the `AlertManager` singleton class that handles the business logic
- `test.py` handles the testing and runs via `pytest`

### Usage:
- `alerts = AlertManager.getInstance()` can be used to get the instance of the `AlertManager`
- `alerts.send_alert("<your-alert-here>")` can be used to send in your alert

### Testing the function for correctness:
- Run `pytest test.py` in your terminal to see the test results
- Edit `test.py` to observe class behavior/add more tests to suit your needs

### Questions:

- ##### How would you architect things differently if the time interval needed to be different depending on the event?
  I would update the config dictionary based on the alert message and use it based on the alert I receive.

- ##### How would you architect things differently if the debouncing needs to happen across multiple processes?
  As I maintain a singleton class to maintain the state of the alert message being shown, multiple processes would be handled as well without colliding with each other as they would reach for the same instance of the class. It is already implemented.
