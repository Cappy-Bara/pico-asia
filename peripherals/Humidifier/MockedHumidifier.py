from peripherals.Humidifier.Humidifier import Humidifier

class MockedHumidifier(Humidifier):

    def __init__(self, name):
        self.is_working = False
        self._name = name

    def start_working(self):
        self.is_working = True
        print(f"HUMIDIFIER {self._name} IS ON.")

    def stop_working(self):
        self.is_working = False
        print(f"HUMIDIFIER {self._name} IS OFF.")