from states.Conditions import Conditions
from states.ConditionsTimeFrame import ConditionsTimeFrame
from states.ConditionsTimeline import ConditionsTimeline

NATTO = [
    (40,85,60*6),
    (41,84,60),
    (42,83,60),
    (45,82,60),
    (46,81,60),
    (47,80,60),
    (48,79,60),
    (49,78,60),
    (50,77,60),
    (49,76,60),
    (48,75,60),
    (47,72,60),
    (45,69,60),
    (43,66,60),
    (41,63,60),
    (40,60,60),
    (30,57,60),
    (20,55,2*60)
]

TEMPEH = [
    (40,85,60*6),
    (41,84,60),
    (42,83,60),
    (45,82,60),
    (46,81,60),
    (47,80,60),
    (48,79,60),
    (49,78,60),
    (50,77,60),
    (49,76,60),
    (48,75,60),
    (47,72,60),
    (45,69,60),
    (43,66,60),
    (41,63,60),
    (40,60,60),
    (30,57,60),
    (20,55,2*60)
]

YOGHURT = [
    (40,85,60*6),
    (41,84,60),
    (42,83,60),
    (45,82,60),
    (46,81,60),
    (47,80,60),
    (48,79,60),
    (49,78,60),
    (50,77,60),
    (49,76,60),
    (48,75,60),
    (47,72,60),
    (45,69,60),
    (43,66,60),
    (41,63,60),
    (40,60,60),
    (30,57,60),
    (20,55,2*60)
]

def get_timeline(definiton):
    timeframes = list(map(lambda x: ConditionsTimeFrame(x[2],Conditions(x[0],x[1])),definiton))
    return ConditionsTimeline(timeframes,2,5)