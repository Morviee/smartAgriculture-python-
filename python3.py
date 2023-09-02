import RPi.GPIO as GPIO
import time
import datetime
import paho.mqtt.client as mqtt

servoPIN = 17
channel = 21
GPIO setmode(GPIO.BCM) 
GPIO setwarnings(False)
GPIO setup(servoPIN, GPIO.OUT) 
GPIO setup(channel, GPIO.IN)
p = GPIO.PWM(servoPIN, 30)	# GPIO 17 for PWM with 50Hz p.start(3.5)	
p.start(3.5)


def on_connect(client, userdata, flags, rc):
    if rc = 0:
        print("Connected success")
    else:
        print(f"Connected fail with code {rc}")

client = mqtt.Client() 
client.on_connect = on_connect

client connect("broker.hivemq.com", 1880, 60)
#def on_connect(client, userdata, flags, rc):
# print("Connected with result code rc")
def callback(channel):
    if GPIO.input(channel):
        x = datetime.datetime.now()
        final_status_1 = "Timestamp = "+str(x)+" Message = PI-No Water Detected" 
        client.publish('KJSIEIT-SAS-48', payload=final_status_1, qos=0, retain=False) 
        print("No Water Detected")
        p.ChangeDutyCycle(4)	#switch off (-90 degree) time.sleep(5)
    else:
        x = datetime.datetime.now()
        final_status = "Timestamp = "+str(x)+" Message = PI-Water Detected" 
        client.publish('KJSIEIT-SAS-48', payload=final_status, qos=0, retain=False) 
        print("Water Detected")
        p.ChangeDutyCycle(10)	#switch off (90 degree) time.sleep(1)
        time.sleep(1)

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)	# let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)	# assign function to GPIO PIN, Run function on change time.sleep(1)
while True:
    time.sleep(1)
GPIO.cleanup()
