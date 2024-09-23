from machine import I2C, Pin
import time

DEFAULT_I2C_ADDRESS = 0x44

class SHT30:
    def __init__(self, i2c, i2c_address=DEFAULT_I2C_ADDRESS):
        if not isinstance(i2c, I2C):
            raise ValueError("An I2C object is required.")
        self.i2c = i2c
        self.i2c_addr = i2c_address
        time.sleep_ms(50)

    def is_present(self):
        """
        Check if sensor is connected
        """
        return self.i2c_addr in self.i2c.scan()

    def send_cmd(self, cmd_request, response_size=6, read_delay_ms=100):
        """
        Send command and read response from SHT30 sensor.
        """
        try:
            self.i2c.writeto(self.i2c_addr, cmd_request)  # Send command to the sensor
            if not response_size:
                return
            time.sleep_ms(read_delay_ms)  # Wait for sensor to process
            data = self.i2c.readfrom(self.i2c_addr, response_size)  # Read the response
            return data
        except OSError as e:
            raise RuntimeError("I2C communication error") from e