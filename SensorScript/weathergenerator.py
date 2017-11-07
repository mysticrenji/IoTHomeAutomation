import Adafruit_DHT
import ssl
import sys
import paho.mqtt.client as mqtt
import time
from time import sleep
from datetime import date, datetime

sensor = Adafruit_DHT.DHT22
pin = 4  # GPIO 21
delaySecondsBetweenPublish = 1

mqttCert_Protocol = ssl.PROTOCOL_TLSv1_2
mqttTopic_pub = "IoTSensor/Sensors"
mqttTopic_sub = "IoTSensor/Subscribe"
mqttCert_ca = "/home/pi/IOT/AWSIoT/root-CA.crt"
mqttCert = "/home/pi/IOT/AWSIoT/IoTSensor.cert.pem"
mqttCert_priv = "/home/pi/IOT/AWSIoT/IoTSensor.private.key"
mqttClientId = "IoTSensor"
mqttEndpoint = "aXXXXXXXX.iot.us-west-2.amazonaws.com"
mqttPort = 8883

def on_connect(mqttc, obj, flags, rc):
    if rc == 0:
        print("Client conntected : " + str(rc) + " | Connection status: successful.")
        mqttClient.subscribe(mqttTopic_sub, qos=0)
        publish_data()

def publish_data():
    time.sleep(delaySecondsBetweenPublish)
    now = datetime.utcnow()
    now_str = now.strftime('%Y-%m-%dT%H:%M:%SZ')
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        #payload = '{ "timestamp": "' + now_str + '","temperature": ' + str(result.temperature) + ',"humidity": '+ str(result.humidity": '+ str(result.humidity) '+'  }'
        payload = '{{"timestamp":"{0}","humidity":{1:0.1f},"temperature":{2:0.1f}}}'.format(now_str,humidity,temperature)
        print("Publish {0}".format(payload))
        mqttClient.publish(mqttTopic_pub, payload, 0)

def on_disconnect(client, userdata, rc):
    print("Client connection closed.")

def on_log(pahoClient, obj, level, string):
    print("---------------")
    print(string)

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))
    publish_data()

def teardown():
    mqttClient.disconnect()
    mqttClient.loop_stop()
    sys.exit()

mqttClient = mqtt.Client(client_id=mqttClientId)
mqttClient.on_connect = on_connect
mqttClient.on_disconnect = on_disconnect
mqttClient.on_publish = on_publish
mqttClient.on_log = on_log

mqttClient.tls_set(mqttCert_ca, certfile=mqttCert, keyfile=mqttCert_priv, tls_version=mqttCert_Protocol, ciphers=None)

print("Start connecting to " + mqttEndpoint + ":" + str(mqttPort) + " ...")

try:
    mqttClient.connect(mqttEndpoint, port=mqttPort)
    mqttClient.loop_forever()
except (KeyboardInterrupt, SystemExit):
    teardown()
