# Linux Test Environment

This project uses Linux as a test and integration environment for the
Smart Heating Controller.

The Linux environment is used to:

- run Python and pytest-based automated tests
- run the MQTT broker using Docker
- inspect processes and network connections
- troubleshoot MQTT communication problems
- analyse logs during test failures
- verify that required services and ports are available

## Test Environment

- Python
- pytest
- MQTT
- Mosquitto
- Docker
- Linux

MQTT broker:
- Port: 1883

## Troubleshooting Approach

When an integration test fails:

1. Check the test failure
2. Check whether the MQTT broker is running
3. Check whether port 1883 is available
4. Check running processes and containers
5. Inspect broker logs
6. Identify the root cause
7. Apply the corrective action
8. Re-run the automated tests
9. Verify that the system is working again