import json
import threading


class Properties:
    __instance = None
    __lock = threading.Lock()
    __env: dict = {}

    def __init__(self):
        if Properties.__instance is not None:
            raise Exception('singleton class')
        else:
            Properties.__instance = self

    @staticmethod
    def get_instance():
        if Properties.__instance is None:
            with Properties.__lock:
                if Properties.__instance is None:
                    f = open('app.json')
                    Properties.__env = json.load(f)
                    f.close()
                    Properties()
        return Properties.__instance

    def get_env(self) -> dict:
        return self.__env
