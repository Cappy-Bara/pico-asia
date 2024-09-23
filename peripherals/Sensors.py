from peripherals import TempAndHumSensor

class Sensors:
    def __init__(self, temperature_sensor:TempAndHumSensor):
        self.temperature_reader = temperature_sensor