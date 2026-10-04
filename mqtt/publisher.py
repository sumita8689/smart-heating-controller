import paho.mqtt.client as mqtt
import time

client =mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)
print("Connected")
client.loop_start()
try:
    while True:
        result = client.publish("sumita/heating/temperature",str(18.5))
        print("Publish result:", result.rc)
        time.sleep(2)

except KeyboardInterrupt:
    print("Temperature publisher stopped")

finally:
    client.loop_stop()
    client.disconnect()