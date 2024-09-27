from machine import Pin, I2C
from peripherals import RealTempAndHumSensor, RealHumidifier, RealHeater, RealFan, Sensors
from peripherals.Actuators import Actuators
from peripherals.Button.RealButton import RealButton
from peripherals.Display.RealDisplay import RealDisplay

#   REAL
def get_real_button():
    return RealButton(12,100,2000)

def get_real_display():
    display_i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=400000)
    return RealDisplay(display_i2c,128,64)

def get_real_sensors():
    sensor_i2c = I2C(1, scl=Pin(11), sda=Pin(10), freq=100000)
    tempAndHumSensor = RealTempAndHumSensor(sensor_i2c)
    return Sensors(tempAndHumSensor)

def get_real_actuators():
    fans = RealFan(19)
    humidifier = RealHumidifier(20)
    heater = RealHeater(21)
    return Actuators(heater,fans,humidifier)

def get_real_devices():
    return get_real_button(), get_real_display(), get_real_sensors(), get_real_actuators()