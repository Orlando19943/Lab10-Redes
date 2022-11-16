from common import *
from serial import serializers
from kafka import KafkaProducer
import random
from time import sleep

TIMEOUT = 10

producer = KafkaProducer(bootstrap_servers=SERVER, value_serializer=serializers.JSON)


def clip(lower, value, upper):
    return max(min(upper, value), lower)


def get_data():
    humidity = random.normalvariate(mu=50, sigma=20)
    temperature = random.normalvariate(mu=50, sigma=20)

    # avoid numbers out of range
    humidity = clip(0.00, round(humidity, 2), 100.00)
    temperature = clip(0, int(temperature), 100)

    return SensorData(
        temperature,
        humidity,
        wind_direction=random.choice(list(Direction)),
    )


while True:
    data = get_data()
    print(f"SENDING: {data}")
    producer.send(TOPIC, data).get(TIMEOUT)
    sleep(TIMEOUT)
