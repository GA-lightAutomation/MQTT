import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    #The message parameter is a message class with members topic, qos, payload, retain
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    client.publish("inTopic","ON")

broker_address="127.0.0.1"
client = mqtt.Client("windows") #create new instance
client.connect(broker_address)

client.on_message=on_message #attach function to callback
client.subscribe('keypad')
client.loop_forever()