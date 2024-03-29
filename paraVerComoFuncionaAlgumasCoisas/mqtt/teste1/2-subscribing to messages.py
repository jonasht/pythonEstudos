
import random
from paho.mqtt import client as mqtt_client

broker = 'localhost'
port = 1883
topic = "teste"

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'

username = 'teste'
password = '123'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print('conectado ao mqtt Broker')

        else:
            print(f'falha ao conectar, retorne code {rc}')

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f'recebendo {msg.payload.decode()} from {msg.topic} topic')

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()