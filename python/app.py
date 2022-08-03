import paho.mqtt.client as mqtt
import sqlite3

con = sqlite3.connect('door.db', check_same_thread=False)
cur = con.cursor()

def testDB():
    for row in cur.execute("SELECT * FROM test"):
        print(row)

def authenticate(access,key): #check if user credentials exist
    user=0
    for row in cur.execute(f"SELECT * FROM users WHERE {access}='{key}'"):
        print(row)
        user+=1
    if user:
        client.publish("ACK","OPEN")
    else :
        print("DENIED ACCESS")
        client.publish("ACK","CLOSE")

def on_message(client, userdata, message):
    #The message parameter is a message class with members topic, qos, payload, retain
    #testDB()
    authenticate(message.topic,str(message.payload.decode("utf-8")))

broker_address="192.168.100.12"
client = mqtt.Client("windows") #create new instance
client.connect(broker_address)

client.on_message=on_message #attach function to callback
client.subscribe([('keypad',0),('rfid',0)])
client.loop_forever()