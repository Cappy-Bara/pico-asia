from states.ConditionsTimeFrame import ConditionsTimeFrame

class ConditionsTimeline:
    def __init__(self, frames:list[ConditionsTimeFrame], delta_temp:float, delta_hum:float):
        self.whole_time = sum(f.span for f in frames)
        self._current_frame = frames.pop(0)
        self._frames = frames
        self._passed_frames_time = 0
        self.delta_temp = delta_temp
        self.delta_hum = delta_hum

    def get_current_frame(self, passed_time:int):

        if(self._is_frame_finished(passed_time)):
            if(len(self._frames) == 0):
                return None
            self._swap_current_frame()

        return self._current_frame.conditions
    
    def _is_frame_finished(self, passed_time:int):
        return self._current_frame.span + self._passed_frames_time <= passed_time

    def _swap_current_frame(self):
        self._passed_frames_time = self._passed_frames_time + self._current_frame.span
        self._current_frame = self._frames.pop(0)