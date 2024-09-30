from FileWriter import FileWriter
from devices import get_real_devices
from mocked_devices import get_mocked_devices, get_virtual_devices
from selecting_phase import selecting_phase
from states import StateMachine
from time import sleep_ms
from working_phase import working_phase

button,display,sensors,actuators = get_real_devices()

is_finished = False
state_machine = None
file_writer = FileWriter("data.csv")

while not is_finished:
    
    if(state_machine == None):
        selected_program = selecting_phase(button, display)

        if(selected_program is not None):
            state_machine = StateMachine(selected_program,sensors,actuators)
            file_writer.open_file()
        sleep_ms(100)

    else:
        is_finished = working_phase(state_machine,display,file_writer)
        sleep_ms(500)

file_writer.close_file()
display.display_finish()