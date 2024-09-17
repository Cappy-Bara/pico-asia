from SHT30.TempAndHumReader import TempAndHumReader
from machine import I2C, Pin
import time


i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=100000)
tempAndHumReader = TempAndHumReader(i2c)


def validate_pins():
    if tempAndHumReader.is_sensor_connected():
        print("Sensor not detected.")


while True:

    validate_pins()

    temperature, humidity = tempAndHumReader.get_celsius_measurements()
    print(f"Temperature: {temperature:.2f} °C, Humidity: {humidity:.2f} %")
        
    time.sleep_ms(350)

