from peripherals import Sensors
from peripherals.Actuators import Actuators
from peripherals.Button.Button import Button
from peripherals.Button.MockedButton import MockedButton
from peripherals.Display.ConsoleDisplay import ConsoleDisplay
from peripherals.Display.Display import Display
from peripherals.Fan.MockedFan import MockedFan
from peripherals.Heater.MockedHeater import MockedHeater
from peripherals.Humidifier.MockedHumidifier import MockedHumidifier
from peripherals.TempAndHumSensor.MockedTempAndHumSensor import MockedTempAndHumSensor
from peripherals.TempAndHumSensor.VirtualTempAndHumSensor import VirtualTempAndHumSensor

#   MOCKED
def get_mocked_button():
    return MockedButton(100,2000)

def get_mocked_display():
    return ConsoleDisplay()

def get_mocked_sensors():
    tempAndHumSensor = MockedTempAndHumSensor()
    return Sensors(tempAndHumSensor)

def get_virtual_sensors(acutators : Actuators):
    tempAndHumSensor = VirtualTempAndHumSensor(0,0,1,1,acutators.heater, acutators.humidifier)
    return Sensors(tempAndHumSensor)

def get_mocked_actuators():
    fans = MockedFan(19)
    humidifier = MockedHumidifier(20)
    heater = MockedHeater(21)
    return Actuators(heater,fans,humidifier)

def get_mocked_devices():
    return get_mocked_button(), get_mocked_display(), get_mocked_sensors(), get_mocked_actuators()

def get_virtual_devices():
    ac = get_mocked_actuators()
    return get_mocked_button(), get_mocked_display(), get_virtual_sensors(ac), ac