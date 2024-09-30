from states.StateResult import StateResult

class FileWriter():
    def __init__(self, file_name):
        self._file_name = file_name
        self._current_tick = 0

    def should_write(self, tick):
        return tick != self._current_tick

    def open_file(self):
        self._file=open(self._file_name,"w")
        self._file.write("TEMP,HUM\n")
        pass

    def write_data(self, data : StateResult):
        self._current_tick = data.passed_time

        temp = int(data.current_temperature)
        hum = int(data.current_humidity)

        value = f"{temp},{hum}\n"
        self._file.write(value)
        pass

    def close_file(self):
        self._file.close()
        pass

