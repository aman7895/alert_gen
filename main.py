from datetime import datetime as dt, timedelta
from threading import Lock
from config import wait_time


class AlertManager:
    __instance = None
    __allow_object_creation = False
    __message = {}
    __conf = {}
    # Adding a lock variable to implement multithreading
    __lock = Lock()

    # Static method to access the instance as AlertManager is an interface
    @staticmethod
    def getInstance():
        if AlertManager.__instance == None:
            AlertManager.__allow_object_creation = True
            AlertManager()
            # To make sure no new objects can be created
            AlertManager.__allow_object_creation = False
        return AlertManager.__instance

    # Private constructor as we don't want to let any variable create an instance
    def __init__(self):
        if AlertManager.__instance != None or not AlertManager.__allow_object_creation:
            raise Exception("[ERROR] Alert Manager is a singleton!")
        else:
            AlertManager.__instance = self
            self.__conf['wait_time'] = wait_time  # default wait time as config

    def send_alert(self, message) -> bool:
        with self.__lock:
            if message not in self.__message or dt.now() > self.__message[message]:
                self.__message[message] = dt.now() + timedelta(seconds=self.__conf['wait_time'])
                print(f'[INFO] Time: {dt.now()} Message: {message}')
                return True
            return False
