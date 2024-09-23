from states.Conditions import Conditions

class ConditionsTimeFrame:
    def __init__(self, span:int, conditions:Conditions):
        self.span = span
        self.conditions = conditions