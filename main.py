import machine
from machine import Pin, I2C
from display.ssd1306 import SSD1306_I2C
from peripherals.Fan.RealFan import RealFan
from peripherals.Heater.RealHeater import RealHeater
from peripherals.Humidifier.RealHumidifier import RealHumidifier
from peripherals.TempAndHumSensor.RealTempAndHumSensor import RealTempAndHumSensor
import time


WIDTH = 128
HEIGHT = 64

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=400000)
display = SSD1306_I2C(128, 64, i2c)
i2ctemp = I2C(1, scl=Pin(11), sda=Pin(10), freq=100000)
tempAndHumReader = RealTempAndHumSensor(i2ctemp)

heater = RealHeater(19)
fans = RealFan(20)
humidifier = RealHumidifier(21)


while True:
    temperature, humidity = tempAndHumReader.get_celsius_measurements()
    formatted_temp = "{:.1f}".format(temperature)
    formatted_hum = "{:.1f}".format(humidity)

    display.text('Temperature:',0,0)
    display.text(f'{formatted_temp}',0,14)
    display.text('Humidity',0,28)
    display.text(f'{formatted_hum}',0,42)
    display.show()
    display.fill(0)
        
    heater.start_heating()
    fans.start_working()
    water.start_working()

    heater.stop_heating()
    water.stop_working()
    fans.stop_working()