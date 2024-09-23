from peripherals.Fan.Fan import Fan
from peripherals.Heater.Heater import Heater

class MockedFan(Fan):

    def __init__(self, name):
        self.is_working = False
        self._name = name

    def start_working(self):
        self.is_working = True
        print(f"FAN {self._name} IS ON.")

    def stop_working(self):
        self.is_working = False
        print(f"FAN {self._name} IS OFF.")