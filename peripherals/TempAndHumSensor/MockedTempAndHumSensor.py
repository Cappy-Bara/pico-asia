from peripherals.TempAndHumSensor.TempAndHumSensor import TempAndHumSensor

class MockedTempAndHumSensor(TempAndHumSensor):
    def __init__(self):
        self._required_ticks:int = 0
        self._count:int = 1
        self._mocked_temperature:float = 0
        self._mocked_hum:float = 0
        self._temp_gradient:float = 0
        self._hum_gradient:float = 0

    def get_celsius_measurements(self) -> tuple[float,float]:

        if(self._count < self._required_ticks):
            self._count = self._count+1
            self._mocked_temperature=self._mocked_temperature + self._temp_gradient
            self._mocked_hum=self._mocked_hum + self._hum_gradient
            return self._mocked_temperature, self._mocked_hum

        self._mocked_temperature = float(input('MOCKED TEMPERATURE: '))
        self._mocked_hum = float(input('MOCKED HUM: '))
        self._required_ticks = int(input('NUMBER OF TICKS: '))
        self._temp_gradient = int(input('TEMP GRADIENT: '))
        self._hum_gradient = int(input('HUM GRADIENT: '))
        self._count = 1

        return self._mocked_temperature, self._mocked_hum