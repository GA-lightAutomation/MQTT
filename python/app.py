import paho.mqtt.client as mqtt
import time
"""
 Using the paho mqtt client class
Main methods:
conncect() & disconnect()
subscribe() & unsubscribe()
publish()

1.) Create a new instance of client
    <var> = mqtt.Client(<client_name>)
    Client(Client_id="", clean_session=True, userdata=None, protocol=MQTTv3)
2.) Connect client instance to broker
    <var>.connect(<broker_address>)
    connect(host, port=1883, keepalive=60, bind_address="")
3.) Once connection is established one can publish messages
    <var>.publish("<topic>", "<payload>")
    publish(topic, payload=None, qos=0, retain=False)
4.) Subscribing to a topic
    <var>.subscribe("topic")
    subscribe(topic,qos=0)
5.) When a client receives a message, it generates the on_message callback
    To view the messages, one activates and processes the on_message callback
    To process callbacks:
        i)  Create a callback function to process any messages
        ii) Start a loop to check for callback messages
    Attach the callback function to our client object as follows
    <var>.on_message = <callback_function>
6.) Start a loop to process the callback

# Built in logging feature
"""

def on_message(client, userdata, message):
    #The message parameter is a message class with members topic, qos, payload, retain
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    client.publish("inTopic","ON")

broker_address="127.0.0.1"
print("creating new instance")
client = mqtt.Client("pypi") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("outTopic")
print("Publishing message to topic","inTopic")
client.publish("inTopic","ON")
time.sleep(10) # wait
#client.loop_stop() #stop the loop