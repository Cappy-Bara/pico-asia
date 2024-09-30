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

        self._temp_buffer = []
        self._hum_buffer = []

    def stop(self):
        self._actuators.fan.stop_working()
        self._actuators.heater.stop_heating()
        self._actuators.humidifier.stop_working()

    def handle(self):

        time = self.get_passed_time()
        required_conditions = self._timeline.get_current_frame(time)

        if(required_conditions is None):
            self.stop()
            return None

        curr_temp, curr_hum = self._sensors.temp_hum_sensor.get_celsius_measurements()

        self._temp_buffer.append(curr_temp)
        self._hum_buffer.append(curr_hum)

        if(len(self._temp_buffer) > 5):
            self._temp_buffer.pop(0)
            self._hum_buffer.pop(0)

        mean_temp = sum(self._temp_buffer) / len(self._temp_buffer)
        mean_hum = sum(self._hum_buffer) / len(self._hum_buffer)

        self.handle_actuators(required_conditions, mean_temp,self._timeline.delta_temp, mean_hum, self._timeline.delta_hum)

        return StateResult(mean_temp, mean_hum, self._actuators.heater.is_working,
                           self._actuators.humidifier.is_working, self._actuators.fan.is_working, time,
                           required_conditions.temperature, required_conditions.humidity)
    
    def get_passed_time(self):
        return (int)((time.time() - self._start_time)/60)

    def handle_actuators(self, required_conditions : Conditions, curr_temp:float, d_temp:float, curr_hum:float, d_hum:float):

        req_temp = required_conditions.temperature
        req_hum = required_conditions.humidity

        heater_is_working = self._actuators.heater.is_working
        humidifier_is_working = self._actuators.humidifier.is_working

        should_heater_be_on = (heater_is_working and curr_temp < req_temp) or (not heater_is_working and curr_temp < req_temp-d_temp)
        should_humidifier_be_on = (humidifier_is_working and curr_hum < req_hum) or (not humidifier_is_working and curr_hum < req_hum-d_hum)
        should_fan_be_on = ((curr_hum > req_hum+10) and not self._actuators.fan.is_working) or ((curr_hum > req_hum+2) and self._actuators.fan.is_working) or ((curr_temp > req_temp+5) and not self._actuators.fan.is_working) or ((curr_temp > req_temp) and self._actuators.fan.is_working)
        
        self._actuators.heater.start_heating() if should_heater_be_on else self._actuators.heater.stop_heating()
        self._actuators.fan.start_working() if should_fan_be_on else self._actuators.fan.stop_working()
        self._actuators.humidifier.start_working() if should_humidifier_be_on else self._actuators.humidifier.stop_working()