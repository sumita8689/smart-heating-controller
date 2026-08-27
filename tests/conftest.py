import pytest,threading
import paho.mqtt.client as mqtt
from mqtt.subscriber import on_connect, on_msg
from heating_controller import HeatingController

@pytest.fixture(scope="function")
def controller():
    return HeatingController(target_temp=21,hysteresis=0.5)

@pytest.fixture(scope="function")
def mqtt_fixture(controller):
    event1 = threading.Event()
    event2 = threading.Event()
    data = {'controller': controller, 'event_subscribe': event1, 'event_process': event2, 'action': 'OFF'}
    client_subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, userdata=data)
    client_subscriber.on_connect = on_connect
    client_subscriber.on_message = on_msg
    client_subscriber.connect("localhost", 1883)
    client_subscriber.loop_start()
    assert event1.wait(5)
    client_publisher = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client_publisher.connect("localhost", 1883)
    print("Connected")
    client_publisher.loop_start()
    yield client_publisher,data,event2
    client_publisher.loop_stop()
    client_publisher.disconnect()
    client_subscriber.loop_stop()
    client_subscriber.disconnect()