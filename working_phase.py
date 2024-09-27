from peripherals.Display.Display import Display
from states.StateMachine import StateMachine

def working_phase(state_machine: StateMachine, display : Display):
    result = state_machine.handle()
    
    if(result is None):
        return True

    display.display_state(state_machine._timeline.whole_time,result)

    return False