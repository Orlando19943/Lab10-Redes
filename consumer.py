from common import *
from kafka import KafkaConsumer
from serial import deserializers
from collections import deque
import matplotlib.pyplot as plt

MAX_DOTS = 100

# DATA STRUCTURES
temperatures = deque([], MAX_DOTS)
humidity = deque([], MAX_DOTS)
wind_direction = deque([], MAX_DOTS)
x = deque([], MAX_DOTS)

# GRAPHING STUFF
plt.style.use("seaborn-darkgrid")
top_left = plt.subplot2grid((2, 2), (0, 0))
top_right = plt.subplot2grid((2, 2), (0, 1))
bottom = plt.subplot2grid((2, 2), (1, 0), colspan=2)
plt.ion()


def render():
    top_left.set_title(f"Temperatura: {temperatures[-1]}")
    top_left.plot(x, temperatures, color="red")
    top_left.get_xaxis().set_visible(False)

    top_right.set_title(f"Humedad: {humidity[-1]}")
    top_right.plot(x, humidity, color="blue")
    top_right.get_xaxis().set_visible(False)

    bottom.set_title(f"Dirección del Viento: {wind_direction[-1]}")
    bottom.step(x, wind_direction, where='post', color='green')
    bottom.get_xaxis().set_visible(False)

    plt.pause(0.5)


# START LISTENING THE SERVER
consumer = KafkaConsumer(TOPIC, bootstrap_servers=SERVER, value_deserializer=deserializers.JSON)
for mensaje in consumer:
    temperatures.append(mensaje.value.temperature)
    humidity.append(mensaje.value.humidity)
    wind_direction.append(mensaje.value.wind_direction.name)
    if len(x) == 0:
        x.append(0)
    else:
        x.append(x[-1] + 1)
    print(mensaje.value)
    render()
