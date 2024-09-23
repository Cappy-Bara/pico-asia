from libs.SHT30.SHT30 import SHT30
from machine import I2C
from peripherals.TempAndHumSensor.TempAndHumSensor import TempAndHumSensor

DEFAULT_I2C_ADDRESS = 0x44
MEASUREMENT_COMMAND = b'\x2C\x10'
MEASUREMENT_SIZE = 6

class RealTempAndHumSensor(TempAndHumSensor):
    def __init__(self, i2c, delta_temp=0, delta_hum=0, i2c_address=DEFAULT_I2C_ADDRESS):
        
        if not isinstance(i2c, I2C):
            raise ValueError("An I2C object is required.")
        
        self.SHT30 = SHT30(i2c,i2c_address)
        self.delta_temp = delta_temp
        self.delta_hum = delta_hum

    def is_sensor_connected(self):
        """
        Check if sensor is connected
        """
        return self.SHT30.is_present()

    def get_celsius_measurements(self):
        """
        Get temperature and humidity from the sensor.
        """
        data = self.SHT30.send_cmd(MEASUREMENT_COMMAND, MEASUREMENT_SIZE)
        if data:
            celsiusTemp = (((data[0] << 8) | data[1]) * 175 / 65535) - 45  # Temperature in °C
            percentHum = ((data[3] << 8 | data[4]) * 100) / 65535  # Humidity in %
            return celsiusTemp + self.delta_temp, percentHum + self.delta_hum
        else:
            raise RuntimeError("Failed to read data from sensor")