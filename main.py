from machine import Pin, I2C
from display.ssd1306 import SSD1306_I2C
from peripherals import RealTempAndHumSensor, RealHumidifier, RealHeater, RealFan, Sensors
from peripherals.Actuators import Actuators
from peripherals.TempAndHumSensor.MockedTempAndHumSensor import MockedTempAndHumSensor
from peripherals.TempAndHumSensor.VirtualTempAndHumSensor import VirtualTempAndHumSensor
from states import ConditionsTimeFrame, ConditionsTimeline, Conditions, StateMachine
from time import sleep

def get_timeline():
    con1 = Conditions(50,50)
    con1f = ConditionsTimeFrame(10,con1)
    con2 = Conditions(60,60)
    con2f = ConditionsTimeFrame(10,con2)
    con3 = Conditions(70,70)
    con3f = ConditionsTimeFrame(10,con3)
    con4 = Conditions(80,80)
    con4f = ConditionsTimeFrame(10,con4)

    return ConditionsTimeline([con1f,con2f,con3f,con4f],10,10)


####REAL DEVICES
# i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=400000)
# display = SSD1306_I2C(128, 64, i2c)

# i2ctemp = I2C(1, scl=Pin(11), sda=Pin(10), freq=100000)
# tempAndHumSensor = RealTempAndHumSensor(i2ctemp)

# heater = RealHeater(19)
# fans = RealFan(20)
# humidifier = RealHumidifier(21)

####MOCKED DEVICES
# tempAndHumSensor = MockedTempAndHumSensor()
heater = RealHeater(19)
fans = RealFan(20)
humidifier = RealHumidifier(21)
tempAndHumSensor = VirtualTempAndHumSensor(35,35,2,2,heater,humidifier)

actuators = Actuators(heater,fans,humidifier)
sensors = Sensors(tempAndHumSensor)

timeline = get_timeline()

stateMachine = StateMachine(timeline,sensors,actuators)

while True:
    result = stateMachine.handle()
    print(f'TIME:{result.passed_time}')
    print(f'TEMP:{result.current_temperature}')
    print(f'HUM:{result.current_humidity}')
    sleep(0.25)