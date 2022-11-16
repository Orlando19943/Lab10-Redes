import json
from common import Direction, SensorData


def JSON(v: SensorData):
    b = json.dumps({
        'temp': v.temperature,
        'humidity': v.humidity,
        'wind': v.wind_direction.name,
    })
    return b.encode('utf-8')


def __compact(v, bits):
    return format(v, 'b')[:bits].zfill(bits)


def COMPACT(v: SensorData):
    # 14 bits - para temp 0.00-100.00
    # 7 bits - para humedad 0-100
    # 3 bits - para dirección del viento 0-7
    temp = __compact(int(v.temperature * 100), 14)
    humidity = __compact(v.humidity, 7)
    wind = __compact(v.wind_direction.value, 3)

    binary = temp + humidity + wind

    # Convert bitstring to bytes
    return int(binary, 2).to_bytes(3, byteorder='big')
