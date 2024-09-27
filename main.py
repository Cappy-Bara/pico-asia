from machine import Pin, I2C
from display.ssd1306 import SSD1306_I2C
from peripherals import RealTempAndHumSensor, RealHumidifier, RealHeater, RealFan, Sensors
from peripherals.Actuators import Actuators
from peripherals.Button.RealButton import RealButton
from peripherals.TempAndHumSensor.MockedTempAndHumSensor import MockedTempAndHumSensor
from peripherals.TempAndHumSensor.VirtualTempAndHumSensor import VirtualTempAndHumSensor
from states import ConditionsTimeFrame, ConditionsTimeline, Conditions, StateMachine
from time import sleep, sleep_ms

def get_timeline():
    con1 = Conditions(40,40)
    con1f = ConditionsTimeFrame(1,con1)
    return ConditionsTimeline([con1f],5,5)

def natto_timeline():
    con1 = Conditions(40,85)
    con1f = ConditionsTimeFrame(60*6,con1)

    con2 = Conditions(41,84)
    con2f = ConditionsTimeFrame(60,con2)

    con3 = Conditions(42,83)
    con3f = ConditionsTimeFrame(60,con3)

    con4 = Conditions(45,82)
    con4f = ConditionsTimeFrame(60,con4)

    con5 = Conditions(46,81)
    con5f = ConditionsTimeFrame(60,con5)

    con6 = Conditions(47,80)
    con6f = ConditionsTimeFrame(60,con6)

    con7 = Conditions(48,79)
    con7f = ConditionsTimeFrame(60,con7)

    con8 = Conditions(49,78)
    con8f = ConditionsTimeFrame(60,con8)
    
    con9 = Conditions(50,77)
    con9f = ConditionsTimeFrame(60,con9)

    con10 = Conditions(49,76)
    con10f = ConditionsTimeFrame(60,con10)

    con11 = Conditions(48,75)
    con11f = ConditionsTimeFrame(60,con11)

    con12 = Conditions(47,72)
    con12f = ConditionsTimeFrame(60,con12)

    con13 = Conditions(45,69)
    con13f = ConditionsTimeFrame(60,con13)

    con14 = Conditions(43,66)
    con14f = ConditionsTimeFrame(60,con14)

    con15 = Conditions(41,63)
    con15f = ConditionsTimeFrame(60,con15)

    con16 = Conditions(40,60)
    con16f = ConditionsTimeFrame(60,con16)

    con17 = Conditions(30,57)
    con17f = ConditionsTimeFrame(60,con17)

    con18 = Conditions(20,55)
    con18f = ConditionsTimeFrame(2*60,con18)

    return ConditionsTimeline([con1f,con2f,con3f,con4f,con5f,con6f,con7f,con8f,con9f,con10f,
                               con11f,con12f,con13f,con14f,con15f,con16f,con17f,con18f],5,5)

# ##REAL DEVICES
i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=400000)
display = SSD1306_I2C(128, 64, i2c)

i2ctemp = I2C(1, scl=Pin(11), sda=Pin(10), freq=100000)
tempAndHumSensor = RealTempAndHumSensor(i2ctemp)

fans = RealFan(19)
humidifier = RealHumidifier(20)
heater = RealHeater(21)

actuators = Actuators(heater,fans,humidifier)
sensors = Sensors(tempAndHumSensor)

timeline = natto_timeline()
stateMachine = StateMachine(timeline,sensors,actuators)

button = RealButton(12,100,2000)

def working_phase():
    result = stateMachine.handle()
    if(result is None):
        return True

    formatted_temperature = "{:.1f}".format(result.current_temperature)
    formatted_hum = "{:.1f}".format(result.current_humidity)

    req_temp = "{:.1f}".format(result.required_temp)
    req_hum = "{:.1f}".format(result.required_hum)

    display.text(f'TEM:{formatted_temperature}->{req_temp}',0,0)
    display.text(f'HUM:{formatted_hum}->{req_hum}',0,14)
    display.text(f'TIME: {result.passed_time}/{stateMachine._timeline.whole_time}',0,42)
    display.show()
    display.fill(0)
    sleep(0.5)
    return False

programs = ['TEMPEH','NATTO','JOGURT']
previous_program = programs[0]
current_program = programs[1]
program_id = 1

def selecting_phase():
    global program_id, current_program, previous_program
    button.check_status()
    if(button.is_long_press):
        return True

    if(button.is_short_press):
        program_id = program_id+1 if program_id < 2 else 0
        current_program = programs[program_id]
        pass

    if(current_program != previous_program):
        display.text(f'SELECT PROGRAM:',0,0)
        display.text(current_program,0,14)
        display.show()
        display.fill(0)

    previous_program = current_program 
    return False

is_program_selected = False
is_finished = False 

while not is_finished:
    if(not is_program_selected):
        is_program_selected = selecting_phase()
        sleep_ms(100)
    else:
        is_finished = working_phase()



display.text(f'--------------',0,0)
display.text(f'---FINISHED---',0,14)
display.text(f'--------------',0,42)
display.show()