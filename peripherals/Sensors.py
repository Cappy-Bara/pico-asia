from peripherals import TempAndHumSensor

class Sensors:
    def __init__(self, temp_hum_sensor:TempAndHumSensor):
        self.temp_hum_sensor = temp_hum_sensor