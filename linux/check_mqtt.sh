#! /bin/bash
MQTT_HOST="localhost"
MQTT_PORT="1883"
echo "Checking MQTT broker..."
if ss -ltn  | grep -q ":$MQTT_PORT" ; then
	echo "Port $MQTT_PORT is listening."
else
	echo "ERROR: MQTT port $MQTT_PORT is not listening."
	exit 1
fi
if nc -z "$MQTT_HOST" "$MQTT_PORT" ; then 
	echo "MQTT TCP connection successful."
else
	echo "ERROR: Cannot connect to MQTT broker."
	exit 1
fi



