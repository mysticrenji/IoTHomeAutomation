# IoT Home Automation
Home Automation using AWS IoT integrated with Hass.io dasboard

Developed a dashboard for Home Automation and monitoring, using Hass.io. For this project i used two raspberry pi's with one in remote location(India) integrated with Pi Camera and other local
with DHT22 Sensors.AWS IoT SDK has been installed in both the devices.Also for capturing and pushing the live images through MQTT, installed and configured Node-RED JS in remote Pi.
To have continous remotability(SSH/TCP) to the device, i have used third party services like dataplicity and remote3 for this.

Node-RED workflow will continously push the Image data to AWS on an interval of 4 seconds, from the remote device. Similarly the local device, sense room temperature and humidity via DHT22 Sensors connected to Pi's GPIO and then push it to AWS IoT. This task is accomplished using python script which polls the sensor every seconds.

Home assistant dashboard is configured to fetch data through MQTT topics from AWS IoT.These configurations are stored in YAML file contains topic name, encryption keys, credentials etc.

## Installing Home Assistant
There are few requirements for running Home Assistant. Since it runs most of the lib on python 3.4+ , its mandatory. Also Paho MQTT library.

Please follow the below command to fullfill the requirements

$ sudo apt-get install build-essential checkinstall <br>
$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev<br>
$ cd /usr/src <br>
$ wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz <br>
$ sudo tar xzf Python-3.5.2.tgz <br>
$ cd Python-3.5.2 <br>
$ sudo ./configure <br>
$ sudo make altinstall <br>
$ sudo pip install paho-mqtt <br>

After required libraries has been installed, use the guideline from Home Assistant website to install the same
https://home-assistant.io/docs/installation/virtualenv/

## Installing Node-RED in Raspberry Pi
I followed the instructions from the Node-RED official website to do the installation. Its fairly straightforward. In my case i installed in the remote pi device.

https://nodered.org/docs/hardware/raspberrypi

## Architecture
![](https://raw.githubusercontent.com/mysticrenji/IoTHomeAutomation/master/Images/AWS%20Challenge.jpg)

## Node-RED Workflow at remote device
![](https://raw.githubusercontent.com/mysticrenji/IoTHomeAutomation/master/Images/Node-RED.png)

## Demo - Dashboard

### Sample Video
<div align="center">
  <a href="https://www.youtube.com/watch?v=Gy4r200BfIE"><img src="https://img.youtube.com/vi/Gy4r200BfIE/0.jpg" alt="AWS IoT Challenge"></a>
</div>
 

![](https://raw.githubusercontent.com/mysticrenji/IoTHomeAutomation/master/Images/AWS%20Challenge%20-%20Demo.jpg.png)

![](https://raw.githubusercontent.com/mysticrenji/IoTHomeAutomation/master/Images/Demo2.png)

![](https://raw.githubusercontent.com/mysticrenji/IoTHomeAutomation/master/Images/Demo3.png)

![](https://raw.githubusercontent.com/mysticrenji/IoTHomeAutomation/master/Images/MQTT-%20Temp%20&%20Humid.png)
