from peripherals.Button.Button import Button
from peripherals.Display.Display import Display
from states.Conditions import Conditions
from states.ConditionsTimeFrame import ConditionsTimeFrame
from states.ConditionsTimeline import ConditionsTimeline

programs = ['TEMPEH','NATTO','JOGURT']
previous_program = programs[0]
current_program = programs[1]
program_id = 1


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


def selecting_phase(button : Button, display : Display) -> ConditionsTimeline | None:
    global program_id, current_program, previous_program
    button.check_status()
    if(button.is_long_press):
        return natto_timeline()

    if(button.is_short_press):
        program_id = program_id+1 if program_id < 2 else 0
        current_program = programs[program_id]
        pass

    if(current_program != previous_program):
        display.display_program_selecting(current_program)
        
    previous_program = current_program 
    return None