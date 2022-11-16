import json
from common import SensorData, Direction


def JSON(v):
    s = v.decode('utf-8')
    values = json.loads(s)
    return SensorData(
        values['temp'],
        values['humidity'],
        Direction[values['wind']],
    )


def COMPACT(v):
    # convert bytes to bitstring
    b = format(int.from_bytes(v, byteorder='big'), 'b').zfill(24)[:24]

    return SensorData(
        temperature=int(b[:14], 2) / 100,
        humidity=int(b[14:21], 2),
        wind_direction=Direction(int(b[21:], 2))
    )
