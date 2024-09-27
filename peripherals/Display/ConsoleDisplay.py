from peripherals.Display.Display import Display
from states.StateResult import StateResult


class ConsoleDisplay(Display):

    def display_program_selecting(self, current_program):
        print(f'SELECT PROGRAM:',0,0)
        print(current_program,0,14)
    
    def display_state(self, whole_time, result:StateResult):

        formatted_temperature = "{:.1f}".format(result.current_temperature)
        formatted_hum = "{:.1f}".format(result.current_humidity)

        req_temp = "{:.1f}".format(result.required_temp)
        req_hum = "{:.1f}".format(result.required_hum)

        print(f'TEM:{formatted_temperature}->{req_temp}',0,0)
        print(f'HUM:{formatted_hum}->{req_hum}',0,14)
        print(f'TIME: {result.passed_time}/{whole_time}',0,42)
    
    def display_finish(self):
        print(f'--------------',0,0)
        print(f'---FINISHED---',0,14)
        print(f'--------------',0,28)