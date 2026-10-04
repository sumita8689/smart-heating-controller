import paho.mqtt.client as mqtt
import threading

from heating_controller import HeatingController

#MQTT Topics
TEMPERATURE_TOPIC = "sumita/heating/temperature"
TARGET_TOPIC = "sumita/heating/target"
MODE_TOPIC = "sumita/heating/mode"
STATUS_TOPIC = "sumita/heating/status"
CURRENT_TEMPERATURE_TOPIC = "sumita/heating/current_temperature"

def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected to MQTT broker")
    result_temperature = client.subscribe(TEMPERATURE_TOPIC)
    result_target = client.subscribe(TARGET_TOPIC)
    result_mode = client.subscribe(MODE_TOPIC)
    if (result_temperature[0] == mqtt.MQTT_ERR_SUCCESS and result_target[0] == mqtt.MQTT_ERR_SUCCESS and result_mode[0] == mqtt.MQTT_ERR_SUCCESS):
        print("MQTT subscriptions successful")
        userdata["event_subscribe"].set()
    else:
        print("MQTT subscription failed")

def on_msg(client, userdata, message):
    topic= message.topic
    value = message.payload.decode("utf-8")
    # ---------------------------------------------------------
    # 1. TARGET TEMPERATURE FROM HMI
    # ---------------------------------------------------------
    if topic == TARGET_TOPIC:

        try:
            target = float(value)

            userdata["controller"].set_target_temperature(target)

            print(f"Target temperature updated: {target} °C")

        except ValueError as error:
            print(f"Invalid target temperature: {value} - {error}")
        # ---------------------------------------------------------
        # 2. MODE FROM HMI
        # ---------------------------------------------------------
    elif topic == MODE_TOPIC:
        try:
            userdata["controller"].set_mode(value)
            print(f"Mode updated: {value}")
        except ValueError as error:
            print(f"Invalid mode: {value} - {error}")
    # ---------------------------------------------------------
    # 3. CURRENT TEMPERATURE FROM SENSOR/PUBLISHER
    # ---------------------------------------------------------
    elif topic == TEMPERATURE_TOPIC:

        try:
            temp = float(value)
            print(f"Temperature received: {temp} degrees")
            # Send the received temperature to the HMI
            # so that the Current Temperature field is updated.
            client.publish(CURRENT_TEMPERATURE_TOPIC,str(temp))
            # Let the heating controller calculate the action
            action = userdata["controller"].get_action(temp)
            print(f"Heating action: {action}")
            userdata["action"] = action
            # Send the controller result to the HMI
            client.publish(STATUS_TOPIC,str(action))
            # Keep existing test synchronization
            userdata["event_process"].set()
        except ValueError as error:
            print(f"Invalid temperature: {value} - {error}")


def main():
    controller = HeatingController(target_temp=21)
    event_subscribe = threading.Event()
    event_process = threading.Event()

    data = {
        'controller': controller,
        'event_subscribe': event_subscribe,
        'event_process': event_process,
        'action': 'OFF'
    }

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,userdata=data)
    client.on_connect = on_connect
    client.on_message = on_msg
    client.connect("localhost", 1883)
    print("Connected to MQTT broker")
    client.loop_forever()

if __name__ == "__main__":
    main()