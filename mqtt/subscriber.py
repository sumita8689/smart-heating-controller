import paho.mqtt.client as mqtt

from heating_controller import HeatingController


def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected to MQTT broker")
    result = client.subscribe("sumita/heating/temperature")
    if result[0] == mqtt.MQTT_ERR_SUCCESS:
        userdata['event_subscribe'].set()

def on_msg(client, userdata, message):
    temp = float(message.payload.decode("utf-8"))
    print(f"Temperature received: {temp} degrees")
    action = userdata['controller'].get_action(temp)
    print(f"Heating action: {action}")
    userdata['action'] = action
    userdata['event_process'].set()


def main():
    controller = HeatingController(target_temp=21)
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,userdata=controller)
    client.on_connect = on_connect
    client.on_message = on_msg
    client.connect("localhost", 1883)
    client.loop_forever()

if __name__ == "__main__":
    main()