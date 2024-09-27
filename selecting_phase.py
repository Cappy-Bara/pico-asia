from peripherals.Button.Button import Button
from peripherals.Display.Display import Display
from programs import NATTO, TEMPEH, YOGHURT, get_timeline
from states.ConditionsTimeline import ConditionsTimeline

programs = [('TEMPEH', TEMPEH),('NATTO', NATTO),('YOGHURT', YOGHURT)]

previous_program = programs[0]
current_program = programs[1]
program_id = 1

def selecting_phase(button : Button, display : Display) -> ConditionsTimeline | None:
    global program_id, current_program, previous_program
    
    button.check_status()
    if(button.is_long_press):
        return get_timeline(current_program[1])

    if(button.is_short_press):
        program_id = program_id+1 if program_id < 2 else 0
        current_program = programs[program_id]
        pass

    if(current_program != previous_program):
        display.display_program_selecting(current_program[0])
        
    previous_program = current_program 
    return None