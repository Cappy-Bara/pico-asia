import sys
from FileWriter import FileWriter
from devices import get_real_actuators, get_real_button, get_real_devices, get_real_display, get_real_sensors
from mocked_devices import get_mocked_devices, get_mocked_display, get_mocked_sensors, get_virtual_devices, get_virtual_sensors
from selecting_phase import selecting_phase
from states import StateMachine
from states.StateResult import StateResult
from time import sleep_ms
from working_phase import working_phase

button,display,sensors,actuators = get_real_devices()

# button = get_real_button()
# display = get_real_display()
# actuators = get_real_actuators()
# sensors = get_virtual_sensors(actuators)

is_finished = False
state_machine = None
file_writer = FileWriter("data.csv")
err_file = FileWriter("err.log")
num = 0

while not is_finished:
    try:

        if(state_machine == None):
            selected_program = selecting_phase(button, display)

            if(selected_program is not None):
                state_machine = StateMachine(selected_program,sensors,actuators)
                file_writer.open_file()
                file_writer.write_text("TEMP,HUM\n")

            sleep_ms(100)

        else:
            is_finished = working_phase(state_machine,display,file_writer)
            sleep_ms(500)

    except Exception as e:
        num = num+1
        display.display_error()
        err_file.open_file()
        sys.print_exception(e,err_file._file) # type: ignore
        err_file.write_text(str(num))
        display = get_real_display()


file_writer.close_file()
display.display_finish()
err_file.close_file()