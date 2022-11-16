from common import *
from serial import serializers
from kafka import KafkaProducer
import random
from time import sleep

TIMEOUT = 10

producer = KafkaProducer(bootstrap_servers=SERVER, value_serializer=serializers.JSON)


def get_data():
    return SensorData(
        temperature=round(random.uniform(0, 100), 2),
        humidity=random.randint(0, 100),
        wind_direction=random.choice(list(Direction)),
    )


while True:
    data = get_data()
    print(f"SENDING: {data}")
    producer.send(TOPIC, data).get(TIMEOUT)
    sleep(TIMEOUT)
