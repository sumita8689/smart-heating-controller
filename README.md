# Smart Heating Controller



[![Tests](https://github.com/sumita8689/smart-heating-controller/actions/workflows/tests.yml/badge.svg)](https://github.com/sumita8689/smart-heating-controller/actions/workflows/tests.yml)



A Python-based smart heating controller developed using Test-Driven Development (TDD), extended with MQTT-based IoT communication, Dockerized Mosquitto, and automated integration testing with Pytest and GitHub Actions CI.



## 📋 Overview



This project implements a smart heating controller that determines whether heating should be "HEATING" or "OFF" based on:



- Current temperature

- Target temperature

- Hysteresis

- Operating mode

- Manual override



The project was developed incrementally using the RED-GREEN-REFACTOR TDD cycle.


## 📡 MQTT Communication

The heating controller is extended with MQTT-based communication to simulate an IoT environment. A publisher sends temperature values to the `sumita/heating/temperature` MQTT topic. A Dockerized Mosquitto broker handles the communication, while the subscriber receives the temperature messages and passes them to the `HeatingController` for processing. The resulting heating action (`HEATING` or `OFF`) is then stored and verified through automated MQTT integration tests.

## 🔥 Features



- Target temperature control between 20°C and 30°C

- Configurable hysteresis between 0°C and 5°C

- Operating modes:

  - "COMFORT"

  - "ECO"

  - "AWAY"

- Manual override with "OFF" and "AUTO"

- Temperature input validation

- Target temperature validation

- State-dependent hysteresis behavior

- Automatic heating "HEATING" / "OFF" decisions

- Invalid mode and parameter handling



## 🎯 Control Logic



The controller determines the heating state based on the relationship between the current temperature and the effective target temperature.



The effective target is adjusted according to the selected operating mode:



- COMFORT: target temperature unchanged

- ECO: target temperature − 2°C

- AWAY: target temperature − 5°C



Hysteresis prevents unnecessary switching between HEATING and OFF when the temperature fluctuates around the target.



## 🧪 Testing Strategy



The project was developed using a Test-Driven Development (TDD) approach following the RED-GREEN-REFACTOR cycle.


The test suite covers:



- Valid and invalid target temperatures

- Valid and invalid hysteresis values

- Heating and OFF state transitions

- Hysteresis boundary behavior

- COMFORT, ECO and AWAY operating modes

- Manual override activation and deactivation

- Invalid operating modes and override commands

- Target temperature changes during operation

- Independence between controller instances

- State interactions between operating modes and manual override

### MQTT Integration Testing

MQTT communication is tested using a real Mosquitto broker running in Docker. The integration tests create a subscriber and publisher, exchange temperature messages through the MQTT topic, and verify that the `HeatingController` produces the expected heating action.

The tests use `threading.Event` objects to synchronize the asynchronous MQTT callbacks and ensure that the message has been received and processed before the assertions are evaluated.



### Pytest



The project uses Pytest features including:



- Fixtures via conftest.py

- Parametrized tests

- Exception testing with pytest.raises

- Test discovery and configuration through pytest.ini

- Coverage measurement with pytest-cov

Current test coverage:

**100% statement coverage of `heating_controller.py`**



## 🐳 Dockerized MQTT Broker

The MQTT broker is provided by Eclipse Mosquitto running in a Docker container. The broker exposes port `1883` for MQTT communication between the publisher and subscriber.

For local development, the Mosquitto container is started using Docker, allowing the MQTT integration tests to communicate with the broker through `localhost:1883`.

## 🚀 Continuous Integration



GitHub Actions runs the test suite automatically on every push and pull request.



The CI pipeline:



1. Checks out the repository

2. Sets up Python 3.9

3. Installs the dependencies from `requirements.txt`

4. Starts a Mosquitto MQTT broker in a Docker container

5. Runs the complete Pytest suite

6. Generates the test coverage report



The CI pipeline runs independently of the local development environment using a clean GitHub Actions runner.



## 📁 Project Structure



```text

smart-heating-controller/
├── .github/
│   └── workflows/
│       └── tests.yml
├── mqtt/
│   ├── __init__.py
│   ├── publisher.py
│   └── subscriber.py
├── tests/
│   ├── conftest.py
│   ├── test_heating_controller.py
│   └── test_mqtt_subscriber.py
├── heating_controller.py
├── pytest.ini
├── requirements.txt
└── README.md
```


## ▶️ How to Run
### Windows PowerShell

```powershell

git clone https://github.com/sumita8689/smart-heating-controller.git

cd smart-heating-controller

python -m venv .venv

.venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt

docker run -d -p 1883:1883 eclipse-mosquitto

python -m pytest

```



## 🔴🟢🔵 TDD Development Workflow

The controller was developed incrementally using the RED-GREEN-REFACTOR cycle.



1. RED — Write a failing test for a new requirement.

2. GREEN — Implement the minimum code required to make the test pass.

3. REFACTOR — Improve the implementation or test structure while keeping all tests green.



Examples covered during development include:



- Target temperature validation

- Hysteresis validation

- Operating mode validation

- Manual override behavior

- State transitions

- Hysteresis boundary behavior

- Target temperature changes during operation

- Test parametrization and fixture refactoring



The Git history documents the incremental development process through separate test, implementation, and refactoring commits.



## 📌 Development Highlights



- Developed incrementally using TDD and Git-based RED-GREEN-REFACTOR workflow

- Implemented stateful heating control with hysteresis

- Added operating modes and manual override handling

- Built reusable Pytest fixtures and parametrized validation tests

- Achieved 100% statement coverage for the production controller

- Integrated automated testing into GitHub Actions CI

- Implemented MQTT-based IoT communication with a Dockerized Mosquitto broker and automated integration testing





