from peripherals.Heater.Heater import Heater
from peripherals.Humidifier.Humidifier import Humidifier
from peripherals.TempAndHumSensor.TempAndHumSensor import TempAndHumSensor

class VirtualTempAndHumSensor(TempAndHumSensor):
    def __init__(self,temperature,humidity,temp_speed,hum_speed,heater : Heater, humidifier:Humidifier):
        self._temp_speed:int = temp_speed
        self._hum_speed:int = hum_speed
        self._heater = heater
        self._temperature = temperature
        self._humidity = humidity
        self._humidifier = humidifier

    def get_celsius_measurements(self) -> tuple[float,float]:
        temp_sign = 1 if self._heater.is_working else -1
        hum_sign = 1 if self._humidifier.is_working else -1
        self._temperature = self._temperature + (self._temp_speed * temp_sign)
        self._humidity = self._humidity + (self._hum_speed * hum_sign)
        return self._temperature, self._humidity