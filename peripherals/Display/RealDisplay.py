from libs.SSD1306.ssd1306 import SSD1306_I2C
from peripherals.Display.Display import Display
from states.StateResult import StateResult

class RealDisplay(Display):

    def __init__(self, display_i2c, width, height):
        self._display = SSD1306_I2C(width, height, display_i2c)

    def display_program_selecting(self, current_program):
        self._display.text(f'SELECT PROGRAM:',0,0)
        self._display.text(current_program,0,14)
        self._display.show()
        self._display.fill(0)
    
    def display_state(self, whole_time, result:StateResult):

        formatted_temperature = "{:.1f}".format(result.current_temperature)
        formatted_hum = "{:.1f}".format(result.current_humidity)

        req_temp = "{:.1f}".format(result.required_temp)
        req_hum = "{:.1f}".format(result.required_hum)

        self._display.text(f'TEM:{formatted_temperature}->{req_temp}',0,0)
        self._display.text(f'HUM:{formatted_hum}->{req_hum}',0,14)
        self._display.text(f'TIME: {result.passed_time}/{whole_time}',0,42)
        self._display.show()
        self._display.fill(0)
    
    def display_finish(self):
        self._display.text(f'--------------',0,0)
        self._display.text(f'---FINISHED---',0,14)
        self._display.text(f'--------------',0,28)
        self._display.show()
        self._display.fill(0)