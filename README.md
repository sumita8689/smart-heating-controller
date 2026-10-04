# Smart Heating Controller

A Python-based smart heating controller developed using **Test-Driven Development (TDD)**, **Pytest**, **MQTT**, **Docker**, and **Squish GUI automation**.

The project demonstrates automated testing at multiple levels — from unit testing of the heating logic to MQTT integration testing and end-to-end testing of a Qt-based HMI.

---

## 📌 Project Overview

The Smart Heating Controller simulates a connected heating system.

The system consists of:

- A Python-based heating controller
- MQTT communication using Eclipse Mosquitto
- A Qt-based HMI
- Automated Pytest tests
- MQTT integration tests
- Squish GUI and end-to-end tests
- GitHub Actions CI
- Linux/Docker-based execution

The project was developed following a **RED → GREEN → REFACTOR** TDD approach.

---
# 🚀 Quick Start

Follow these steps to run the complete Smart Heating Controller system locally.

### 1. Clone the repository

```bash
git clone https://github.com/sumita8689/smart-heating-controller.git
cd smart-heating-controller
```

### 2. Create and activate a Python virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the MQTT broker

Start Eclipse Mosquitto using Docker:

```bash
docker run -p 1883:1883 eclipse-mosquitto
```

Verify that the broker is running:

```bash
docker ps
```

Optionally verify the MQTT TCP port:

```bash
nc -zv localhost 1883
```

### 5. Run the automated backend tests

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=. --cov-report=term-missing
```

### 6. Start the MQTT subscriber

Open a new terminal, activate the virtual environment and run:

```bash
python mqtt/subscriber.py
```

### 7. Start the temperature publisher

Open another terminal and run:

```bash
python mqtt/publisher.py
```

The publisher continuously sends simulated temperature data to the MQTT broker.

### 8. Start the Qt HMI

Launch:

```text
SmartHeatingHMI.exe
```

The HMI connects to the MQTT broker and communicates with the Python heating controller.

### 9. Run the Squish GUI tests

Open the Squish IDE and open:

```text
squish/
```

Run the Squish suite to execute:

- GUI tests
- Boundary-value tests
- Data-driven tests
- Synchronization tests
- MQTT backend status tests
- End-to-end heating tests

### Complete system

```text
Docker Mosquitto
       │
       ▼
MQTT Publisher ──────► Python Heating Controller
                              │
                              ▼
                         MQTT Status
                              │
                              ▼
                         Qt HMI
                              │
                              ▼
                       Squish GUI Tests
```
## ✨ Features

- Target temperature control from **20°C to 30°C**
- Heating hysteresis configuration
- Operating modes:
  - COMFORT
  - ECO
  - AWAY
- Manual override
- Heating ON/OFF decision logic
- MQTT-based communication
- Qt-based HMI
- Automated MQTT integration testing
- GUI testing with Squish
- Data-driven testing
- Boundary-value testing
- Asynchronous test synchronization
- Code coverage reporting
- GitHub Actions CI
- Dockerized MQTT broker

---

# 🧠 Heating Controller

The core heating logic is implemented in:

```text
heating_controller.py
```

The controller determines whether the heating system should be:

```text
HEATING
OFF
```

based on:

- Current temperature
- Target temperature
- Hysteresis
- Operating mode
- Manual override

### Operating Modes

| Mode | Behaviour |
|---|---|
| COMFORT | Uses the configured target temperature |
| ECO | Target temperature reduced by 2°C |
| AWAY | Target temperature reduced by 5°C |

Example:

```text
Configured target = 21°C

COMFORT → effective target = 21°C
ECO     → effective target = 19°C
AWAY    → effective target = 16°C
```

---

# 🔄 Test-Driven Development

The project follows the **RED → GREEN → REFACTOR** cycle.

### RED

Write a test for the required behaviour.

```text
Test fails
```

### GREEN

Implement the minimum functionality required.

```text
Test passes
```

### REFACTOR

Improve the implementation while keeping all tests passing.

```text
Clean and maintainable code
```

This approach was used to develop and verify the heating controller behaviour.

---

# 🧪 Pytest Test Automation

The project uses **Pytest** for automated testing.

The test suite covers:

- Target temperature validation
- Boundary values
- Invalid values
- Heating behaviour
- OFF behaviour
- Hysteresis
- Operating modes
- Manual override
- MQTT communication
- MQTT subscriber behaviour
- Integration scenarios

Example:

```bash
pytest
```

---

# 📊 Code Coverage

Code coverage is measured using `pytest-cov`.

Example:

```bash
pytest --cov=. --cov-report=term-missing
```

The production heating controller currently achieves **100% statement coverage**.

Coverage reporting helps identify untested parts of the application and supports continuous improvement of the automated test suite.

---

# 📡 MQTT Integration

The controller communicates using **MQTT** with an Eclipse Mosquitto broker.

The MQTT broker is containerized using Docker.

## MQTT Topics

| Topic | Direction | Purpose |
|---|---|---|
| `sumita/heating/temperature` | Publisher → Controller | Current temperature |
| `sumita/heating/target` | HMI → Controller | Target temperature |
| `sumita/heating/mode` | HMI → Controller | Operating mode |
| `sumita/heating/status` | Controller → HMI | Heating status |
| `sumita/heating/current_temperature` | Controller → HMI | Current temperature for HMI |

### Communication Flow

```text
                 ┌──────────────────────┐
                 │      Qt HMI          │
                 │                      │
                 │ Target Temperature   │
                 │ Operating Mode       │
                 └──────────┬───────────┘
                            │
                            │ MQTT
                            ▼
                 ┌──────────────────────┐
                 │  Mosquitto Broker    │
                 │      Docker          │
                 └──────────┬───────────┘
                            │
                            │ MQTT
                            ▼
                 ┌──────────────────────┐
                 │ Python Subscriber    │
                 │                      │
                 │ HeatingController    │
                 └──────────┬───────────┘
                            │
                            │ HEATING / OFF
                            ▼
                 ┌──────────────────────┐
                 │      Qt HMI          │
                 │    Status Display    │
                 └──────────────────────┘
```

---

# 🐳 Dockerized Mosquitto

The MQTT broker runs inside a Docker container.

Example:

```bash
docker run -p 1883:1883 eclipse-mosquitto
```

Port `1883` is the standard MQTT TCP port.

The Python application connects to:

```text
localhost:1883
```

The TCP connection can be checked with:

```bash
nc -zv localhost 1883
```

This verifies that a service is reachable on TCP port 1883.

---

# 🖥️ Qt HMI

A lightweight Qt-based HMI was developed as the **Application Under Test (AUT)** for GUI automation.

The HMI provides:

- Target temperature selection
- Current temperature display
- COMFORT / ECO / AWAY mode selection
- Apply button
- Reset button
- Heating status
- MQTT connection status

The HMI communicates with the Python backend using MQTT.

### HMI Communication

```text
User
 │
 ▼
Qt HMI
 │
 ├── target temperature ──► MQTT
 │
 ├── operating mode ──────► MQTT
 │
 ◄── current temperature ── MQTT
 │
 ◄── heating status ─────── MQTT
```

The HMI is intentionally lightweight. Its purpose is to provide a realistic GUI for demonstrating automated system and GUI testing.

---

# 🧪 Squish GUI & End-to-End Testing

**Squish for Qt** is used to automate the Qt HMI.

The Squish tests cover GUI behaviour as well as communication between the HMI and the MQTT backend.

The Squish suite is located in:

```text
squish/
```

## Test Areas

### Reset Testing

Verifies that the HMI can reset the configured values correctly.

### Boundary-Value Testing

Tests valid temperature boundaries such as:

```text
20°C
30°C
```

### Data-Driven Testing

Temperature test scenarios are stored in:

```text
squish/tst_test_temperature_data_driven/testdata/temperature_data.csv
```

This allows multiple test cases to be executed using the same test logic.

### Synchronization Testing

The system uses asynchronous MQTT communication.

Squish therefore waits for the expected HMI status before performing the verification.

Example:

```python
result = waitFor(status_is_correct, 5000)

test.verify(
    result,
    "Expected status: " + expected_status
)
```

This avoids race conditions between the GUI and MQTT backend.

### Backend Status Testing

The test verifies that MQTT backend messages are correctly reflected in the HMI.

### End-to-End Heating Test

The end-to-end flow verifies the complete communication chain:

```text
Temperature Publisher
        │
        ▼
   MQTT Broker
        │
        ▼
Python Heating Controller
        │
        ▼
Heating Status
        │
        ▼
   MQTT Broker
        │
        ▼
      Qt HMI
        │
        ▼
Squish Verification
```

This demonstrates testing beyond the GUI itself and validates the interaction between multiple system components.

---

# ♻️ Reusable Squish Test Helpers

Common GUI actions are implemented as reusable helper functions.

Examples:

```python
set_target_temperature()
set_mode()
apply_settings()
verify_status()
```

This keeps individual test cases small and readable and avoids duplicating GUI interaction code.

The helpers are located in:

```text
squish/shared/scripts/heating_helpers.py
```

---

# 🧩 Project Structure

```text
smart-heating-controller/
│
├── heating_controller.py
│
├── mqtt/
│   ├── publisher.py
│   └── subscriber.py
│
├── tests/
│   ├── conftest.py
│   ├── test_heating_controller.py
│   └── test_mqtt_subscriber.py
│
├── squish/
│   ├── config.xml
│   ├── envvars
│   ├── suite.conf
│   │
│   ├── shared/
│   │   └── scripts/
│   │       ├── heating_helpers.py
│   │       └── names.py
│   │
│   ├── tst_test_reset/
│   │   └── test.py
│   │
│   ├── tst_test_boundary_values/
│   │   └── test.py
│   │
│   ├── tst_test_temperature_data_driven/
│   │   ├── test.py
│   │   └── testdata/
│   │       └── temperature_data.csv
│   │
│   ├── tst_test_synchronization/
│   │   └── test.py
│   │
│   ├── tst_test_backend_status/
│   │   └── test.py
│   │
│   └── tst_test_e2e_heating/
│       └── test.py
│
├── linux/
│   └── README.md
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# 🚀 How to Run

## 1. Start Mosquitto

Start the Dockerized MQTT broker:

```bash
docker run -p 1883:1883 eclipse-mosquitto
```

Verify that the broker is running:

```bash
docker ps
```

Optionally verify the MQTT port:

```bash
nc -zv localhost 1883
```

---

## 2. Start the Python Subscriber

From the project root:

```bash
python mqtt/subscriber.py
```

The subscriber connects to the MQTT broker and processes:

```text
temperature
target temperature
operating mode
```

It publishes:

```text
heating status
current temperature
```

---

## 3. Start the Temperature Publisher

Run:

```bash
python mqtt/publisher.py
```

The publisher continuously sends the simulated temperature to:

```text
sumita/heating/temperature
```

The current test publisher sends a temperature value every two seconds.

---

## 4. Start the Qt HMI

Launch:

```text
SmartHeatingHMI.exe
```

The HMI connects to the MQTT broker and displays the heating system status.

---

## 5. Run Pytest

Run the automated backend tests:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=. --cov-report=term-missing
```

---

## 6. Run Squish Tests

Open the Squish IDE and open the suite:

```text
squish/
```

The suite contains GUI, synchronization, data-driven and end-to-end tests for the Qt HMI.

---

# 🔧 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Heating controller and MQTT backend |
| Pytest | Unit and integration testing |
| pytest-cov | Code coverage |
| MQTT | Communication between components |
| Eclipse Mosquitto | MQTT broker |
| Docker | MQTT broker containerization |
| Qt 6 | HMI development |
| C++ / Qt | HMI application |
| Squish for Qt | GUI and system-level automation |
| Git | Version control |
| GitHub | Source code hosting |
| GitHub Actions | Continuous integration |
| Linux | Development and test environment |

---

# 🔄 Continuous Integration

GitHub Actions is used to automatically execute the automated test suite.

The CI pipeline provides:

- Automated test execution
- Regression detection
- Coverage reporting
- Consistent test execution

This ensures that changes to the heating controller and MQTT functionality are automatically validated.

---

# 🎯 Testing Strategy

The project demonstrates multiple levels of testing:

```text
                ┌─────────────────────┐
                │     Squish GUI      │
                │    & E2E Testing    │
                └──────────┬──────────┘
                           │
                ┌──────────▼──────────┐
                │   MQTT Integration  │
                │       Testing       │
                └──────────┬──────────┘
                           │
                ┌──────────▼──────────┐
                │   Pytest Component  │
                │       Testing       │
                └──────────┬──────────┘
                           │
                ┌──────────▼──────────┐
                │ Heating Controller  │
                │      Unit Logic     │
                └─────────────────────┘
```

This combination provides coverage from individual controller logic through to complete GUI-to-backend system behaviour.

---

# 📌 Key Learning Outcomes

Through this project, the following practical skills were demonstrated:

- Test-Driven Development
- Python test automation with Pytest
- MQTT protocol testing
- Asynchronous communication testing
- Docker-based test environments
- Linux command-line usage
- GUI automation with Squish
- Qt HMI testing
- Data-driven testing
- Boundary-value testing
- End-to-end system testing
- Test synchronization
- Reusable automation frameworks
- Code coverage
- CI automation with GitHub Actions

---

# 👩‍💻 Author

**Sumita Melannoor**

Senior Software Test Engineer

GitHub:

`https://github.com/sumita8689`