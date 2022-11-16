from constants import *
from kafka import KafkaConsumer
from serial import deserializers

consumer = KafkaConsumer(TOPIC, bootstrap_servers=SERVER, value_deserializer=deserializers.COMPACT)

for mensaje in consumer:
    print(mensaje.value)