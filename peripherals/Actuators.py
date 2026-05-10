from peripherals import Fan, Humidifier, Heater

class Actuators:
    def __init__(self, heater : Heater, fan : Fan, humidifier : Humidifier):
        self.heater = heater
        self.fan = fan
        self.humidifier = humidifier

    def stop(self):
        self.heater.stop_heating()
        self.fan.stop_working()
        self.humidifier.stop_working()