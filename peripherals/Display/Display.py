from states.StateResult import StateResult

class Display():

    def display_program_selecting(self, current_program):
        raise NotImplementedError
    
    def display_state(self, whole_time, result: StateResult):
        raise NotImplementedError
    
    def display_finish(self):
        raise NotImplementedError