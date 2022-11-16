from enum import Enum
from typing import NamedTuple

TOPIC = "19195"
SERVER = "lab10.alumchat.fun"
PORT = "9092"


class Direction(Enum):
    N = 0
    NE = 1
    E = 2
    SE = 3
    S = 4
    SW = 5
    W = 6
    NW = 7


class SensorData(NamedTuple):
    temperature: float
    humidity: int
    wind_direction: Direction
