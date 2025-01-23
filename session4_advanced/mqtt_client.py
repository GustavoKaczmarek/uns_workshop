# mqtt_client.py

import paho.mqtt.client as mqtt
from data_cache import DataCache
import config

data_cache = DataCache()

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    for topic in config.MQTT_TOPICS:
        client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"Received message: {msg.topic} {msg.payload.decode()}")
    data_cache.update(msg.topic, msg.payload.decode())

def start_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(config.MQTT_BROKER, config.MQTT_PORT, 60)
    client.loop_start()
    return data_cache
