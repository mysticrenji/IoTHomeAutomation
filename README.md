# IoTHomeAutomation
Home Automation using AWS IoT integrated with Hassi.io dasboard

Developed a dashboard for Home Automation and monitoring, using Hass.io. For this project i used two raspberry pi's with one in remote location(India) integrated with Pi Camera and other local
with DHT22 Sensors.AWS IoT SDK has been installed in both the devices.Also for capturing and pushing the live images through MQTT, installed and configured Node-RED JS in remote Pi.
To have continous remotability(SSH/TCP) to the device, i have used third party services like dataplicity and remote3 for this.

Node-RED workflow will continously push the Image data to AWS on an interval of 4 seconds, from the remote device. Similarly the local device, sense room temperature and humidity via DHT22 Sensors connected to Pi's GPIO and then push it to AWS IoT. This task is accomplished using python script which polls the sensor every seconds.

Home assistant dashboard is configured to fetch data through MQTT topics from AWS IoT.These configurations are stored in YAML file contains topic name, encryption keys, credentials etc.

## Architecture
![alt text](IoTHomeAutomation/Images/AWS Challenge.jpg "Abstract view")
