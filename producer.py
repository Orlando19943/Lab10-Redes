from constants import *
from serial import serializers
from kafka import KafkaProducer
import random
from time import sleep


TIMEOUT=10


producer = KafkaProducer(bootstrap_servers=SERVER, value_serializer=serializers.COMPACT)

while True:
    producer.send(TOPIC, {
        'temp': round(random.uniform(0, 100), 2),
        'humidity': random.randint(0, 100),
        'wind': random.choice(WIND_DIRECTIONS)
    }).get(TIMEOUT)
    sleep(TIMEOUT)
