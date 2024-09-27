from devices import get_actuators, get_button, get_display, get_sensors
from selecting_phase import selecting_phase
from states import StateMachine
from time import sleep_ms
from working_phase import working_phase

button = get_button()
display = get_display()
sensors = get_sensors()
actuators = get_actuators()

state_machine = None
is_finished = False 

while not is_finished:
    
    if(state_machine == None):
        selected_program = selecting_phase(button, display)

        if(selected_program is not None):
            state_machine = StateMachine(selected_program,sensors,actuators)
        sleep_ms(100)

    else:
        is_finished = working_phase(state_machine,display)
        sleep_ms(500)

display.display_finish()