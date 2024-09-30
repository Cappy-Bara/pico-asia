from FileWriter import FileWriter
from peripherals.Display.Display import Display
from states.StateMachine import StateMachine

def working_phase(state_machine: StateMachine, display : Display, file_writer: FileWriter):
    result = state_machine.handle()
    
    if(result is None):
        return True

    display.display_state(state_machine._timeline.whole_time,result)

    if(file_writer.should_write(result.passed_time)):
        file_writer.write_data(result)

    return False