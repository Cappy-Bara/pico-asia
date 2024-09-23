import time
from peripherals import Actuators, Sensors
from states import ConditionsTimeline, Conditions
from states.StateResult import StateResult


class StateMachine:
    def __init__(self, timeline: ConditionsTimeline, sensors:Sensors, actuators:Actuators):
        self._sensors = sensors
        self._actuators = actuators
        self._timeline = timeline
        self._was_temp_achieved= False
        self._start_time = time.time()

    def handle(self):

        time = self.get_passed_time()
        required_conditions = self._timeline.get_current_frame(time)
        curr_temp, curr_hum = self._sensors.temp_hum_sensor.get_celsius_measurements()

        self.handle_actuators(required_conditions, curr_temp,self._timeline.delta_temp, curr_hum, self._timeline.delta_hum)

        return StateResult(curr_temp, curr_hum, self._actuators.heater.is_working,self._actuators.humidifier.is_working, self._actuators.fan.is_working, time)
    
    def get_passed_time(self):
        #fix - change to minutes. Seconds for testing purpose
        return time.time() - self._start_time

    def handle_actuators(self, required_conditions : Conditions, curr_temp:float, d_temp:float, curr_hum:float, d_hum:float):

        req_temp = required_conditions.temperature
        req_hum = required_conditions.humidity

        heater_is_working = self._actuators.heater.is_working
        humidifier_is_working = self._actuators.humidifier.is_working

        should_heater_be_on = ((not heater_is_working) and curr_temp < req_temp-d_temp) or (heater_is_working and curr_temp < req_temp)
        should_humidifier_be_on = ((not humidifier_is_working) and curr_hum < req_hum-d_hum) or (humidifier_is_working and curr_hum < req_hum)
        should_fan_be_on = curr_temp > req_temp or curr_hum > req_hum

        self._actuators.heater.start_heating() if should_heater_be_on else self._actuators.heater.stop_heating()
        self._actuators.fan.start_working() if should_fan_be_on else self._actuators.fan.stop_working()
        self._actuators.humidifier.start_working() if should_humidifier_be_on else self._actuators.humidifier.stop_working()