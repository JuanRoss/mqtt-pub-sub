import ssl
import sys
import paho.mqtt.client as mqtt


MQTT_HOST_NAME = 'localhost'
MQTT_HOST_PORT = 1883 

TOPIC = 'installations/water-meters/value'

def onConnect(client, userdata, flags, rc):
    print('connected: %s' % client._client_id)
    client.subscribe(topic=TOPIC, qos=2)

def onMessage(client, userdata, message):
    print('****************')
    print('topic: %s', message.topic)
    print('payload: %s', message.payload)

def main():
    mqttClient = mqtt.Client(client_id='subscriber', clean_session=False)
    mqttClient.connect(host=MQTT_HOST_NAME, port=MQTT_HOST_PORT)
    mqttClient.on_message = onMessage
    mqttClient.on_connect = onConnect
    mqttClient.loop_forever()

if __name__ == '__main__':
    main()
    
