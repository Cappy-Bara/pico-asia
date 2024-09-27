from peripherals.Button.Button import Button
import machine
import utime as time

class RealButton(Button):

    def __init__(self, pinId, short_time, long_time):
        self.is_pressed = False
        self.is_short_press = False
        self.is_long_press = False
        self._previous_state = False
        self._pin = machine.Pin(pinId, machine.Pin.IN, machine.Pin.PULL_UP)
        self._short_time = short_time
        self._long_time = long_time
        self._pressed_time = None

    def check_status(self):
        self.is_pressed = True if self._pin.value() == 0 else False

        if(self.is_pressed and self._previous_state == False):
            self._pressed_time = time.time_ns() // 1_000_000

        passed_time = time.time_ns() // 1_000_000 - self._pressed_time if self._pressed_time is not None else 0

        if(self._previous_state == True and self.is_pressed == False):
            if(passed_time > self._long_time):
                self.is_long_press = True
            elif(passed_time < self._long_time and passed_time > self._short_time):
                self.is_short_press = True

        if(self._previous_state == False and self.is_pressed == False):
            self.is_short_press = False
            self.is_long_press = False

        self._previous_state = self.is_pressed










