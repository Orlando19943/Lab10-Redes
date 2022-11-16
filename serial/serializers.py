import json
from constants import WIND_DIRECTIONS

def JSON(v):
    b = json.dumps(v)
    return b.encode('utf-8')

def compact(v, bits):
    return format(v, 'b')[:bits].zfill(bits)

def COMPACT(v):
    print(f"TRANSLATING: {v}")
    # 14 bits - para temp 0-100.00
    # 7 bits - para humedad 0-100
    # 3 bits - para direccion del viento 0-7
    temp = compact(int(v['temp']*100), 14)
    humidity = compact(v['humidity'], 7)
    wind = compact(WIND_DIRECTIONS.index(v['wind']), 3)

    binary = temp + humidity + wind
    print(f"SENDING {binary}")

    # convert binary to int

    # Convert to bytes
    return int(binary, 2).to_bytes(3, byteorder='big')


