import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f'Connected with result code {rc}')
    client.subscribe("KJSIEIT-SAS-48")# To connect to the code

#This function will run when message will print
def on_message(client, userdata, msg):
    print(f'{msg.topic} {msg.payload}')
    file1 = open("Server_DB_SAS_48_File.txt","a")
    new_message = str(f'\n\n{msg.topic} {msg.payload}\n\n')
    file1.write(new_message)
    file1.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#when the resberry pi will turned off this will send the message to other clients
client.will_set('raspberry/status', b'{"status": "Off"}')

# create connection, the three parameters are broker address, broker port number, and keep-alive time respectively
client.connect("broker.hivemq.com", 1883, 60)

# set the network loop blocking, it will not actively end the program before calling disconnect() or the program crash
client.loop_forever()

