from asyncio import wait_for

from mqtt.subscriber import *


'''class Fakemessage():
    def __init__(self, payload):
        self.payload = payload

msg1 = Fakemessage(b'18')'''
def test_heating_when_target_temp_above_heating_temp(controller,mqtt_fixture):
    client_publisher,data,event2= mqtt_fixture
    result = client_publisher.publish("sumita/heating/temperature", str(18.5))
    print("Publish result:", result.rc)
    result.wait_for_publish()
    print("Message published")
    assert event2.wait(5)
    assert data['action'] == 'HEATING'

def test_heating_when_target_temp_below_heating_temp(controller,mqtt_fixture):
    client_publisher, data, event2 = mqtt_fixture
    result = client_publisher.publish("sumita/heating/temperature", str(30))
    print("Publish result:", result.rc)
    result.wait_for_publish()
    print("Message published")
    assert event2.wait(5)
    assert data['action'] == 'OFF'
