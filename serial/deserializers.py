import json
from constants import WIND_DIRECTIONS

def JSON(v):
    s = v.decode('utf-8')
    return json.loads(s)

def COMPACT(v):
    b = format(int.from_bytes(v, byteorder='big'), 'b').zfill(24)[:24]
    print(f"RECEIVING {b}")
    return {
        "temp": int(b[:14], 2) / 100,
        "humidity": int(b[14:21], 2),
        "wind": WIND_DIRECTIONS[int(b[21:], 2)],
    }
