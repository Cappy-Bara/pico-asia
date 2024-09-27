from peripherals.Display.Display import Display
from states.StateResult import StateResult


class ConsoleDisplay(Display):

    def display_program_selecting(self, current_program):
        print('SELECT PROGRAM:')
        print(current_program)
    
    def display_state(self, whole_time, result:StateResult):

        formatted_temperature = "{:.1f}".format(result.current_temperature)
        formatted_hum = "{:.1f}".format(result.current_humidity)

        req_temp = "{:.1f}".format(result.required_temp)
        req_hum = "{:.1f}".format(result.required_hum)

        print(f'TEM:{formatted_temperature}->{req_temp}')
        print(f'HUM:{formatted_hum}->{req_hum}')
        print(f'TIME: {result.passed_time}/{whole_time}')
    
    def display_finish(self):
        print(f'--------------')
        print(f'---FINISHED---')
        print(f'--------------')