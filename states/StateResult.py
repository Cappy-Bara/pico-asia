class StateResult:
    def __init__(self, current_temperature:float, current_humidity:float, heater_state:bool,
                  humidifier_state:bool, fan_state:bool, passed_time:int, required_temp : float, required_hum : float) -> None:
        self.current_temperature = current_temperature
        self.current_humidity = current_humidity
        self.heater_state = heater_state
        self.humidifier_state = humidifier_state
        self.fan_state = fan_state
        self.passed_time = passed_time
        self.required_temp = required_temp
        self.required_hum = required_hum