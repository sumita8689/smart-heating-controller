import paho.mqtt.client as mqtt


client =mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)
print("Connected")
client.loop_start()
result = client.publish("sumita/heating/temperature", str(18.5))
print("Publish result:", result.rc)

result.wait_for_publish()
print("Message published")
client.loop_stop()
client.disconnect()