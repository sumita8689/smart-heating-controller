\# Smart Heating Controller



\[!\[Tests](https://github.com/sumita8689/smart-heating-controller/actions/workflows/tests.yml/badge.svg)](https://github.com/sumita8689/smart-heating-controller/actions/workflows/tests.yml)



A Python-based heating controller developed using Test-Driven Development (TDD), with Pytest, test coverage, and GitHub Actions CI.



\## Overview



This project implements a smart heating controller that determines whether heating should be "HEATING" or "OFF" based on:



\- Current temperature

\- Target temperature

\- Hysteresis

\- Operating mode

\- Manual override



The project was developed incrementally using the RED-GREEN-REFACTOR TDD cycle.



\## Features



\- Target temperature control between 20°C and 30°C

\- Configurable hysteresis between 0°C and 5°C

\- Operating modes:

&#x20; - "COMFORT"

&#x20; - "ECO"

&#x20; - "AWAY"

\- Manual override with "OFF" and "AUTO"

\- Temperature input validation

\- Target temperature validation

\- State-dependent hysteresis behavior

\- Automatic heating "HEATING" / "OFF" decisions

\- Invalid mode and parameter handling



\## Control Logic



The controller determines the heating state based on the relationship between the current temperature and the effective target temperature.



The effective target is adjusted according to the selected operating mode:



\- COMFORT: target temperature unchanged

\- ECO: target temperature − 2°C

\- AWAY: target temperature − 5°C



Hysteresis prevents unnecessary switching between HEATING and OFF when the temperature fluctuates around the target.



\## Testing Strategy



The project was developed using a Test-Driven Development (TDD) approach following the RED-GREEN-REFACTOR cycle.



The test suite covers:



\- Valid and invalid target temperatures

\- Valid and invalid hysteresis values

\- Heating and OFF state transitions

\- Hysteresis boundary behavior

\- COMFORT, ECO and AWAY operating modes

\- Manual override activation and deactivation

\- Invalid operating modes and override commands

\- Target temperature changes during operation

\- Independence between controller instances

\- State interactions between operating modes and manual override



\### Pytest



The project uses Pytest features including:



\- Fixtures via conftest.py

\- Parametrized tests

\- Exception testing with pytest.raises

\- Test discovery and configuration through pytest.ini

\- Coverage measurement with pytest-cov



Current test coverage:



\*\*100% statement coverage of `heating\_controller.py`\*\*



\## Continuous Integration



GitHub Actions runs the test suite automatically on every push and pull request.



The CI pipeline:



1\. Checks out the repository

2\. Sets up Python 3.9

3\. Installs the dependencies from `requirements.txt`

4\. Runs the complete Pytest suite

5\. Generates the test coverage report



The CI pipeline runs independently of the local development environment using a clean GitHub Actions runner.



\## Project Structure



```text

smart-heating-controller/

├── .github/

│   └── workflows/

│       └── tests.yml

├── tests/

│   ├── conftest.py

│   └── test\_heating\_controller.py

├── .gitignore

├── heating\_controller.py

├── pytest.ini

├── requirements.txt

└── README.md
```


\## How to Run



\### Windows PowerShell





```powershell

git clone https://github.com/sumita8689/smart-heating-controller.git

cd smart-heating-controller

python -m venv .venv

.venv\\Scripts\\Activate.ps1

python -m pip install -r requirements.txt

python -m pytest

```



\## TDD Development Workflow



The controller was developed incrementally using the RED-GREEN-REFACTOR cycle.



1\. RED — Write a failing test for a new requirement.

2\. GREEN — Implement the minimum code required to make the test pass.

3\. REFACTOR — Improve the implementation or test structure while keeping all tests green.



Examples covered during development include:



\- Target temperature validation

\- Hysteresis validation

\- Operating mode validation

\- Manual override behavior

\- State transitions

\- Hysteresis boundary behavior

\- Target temperature changes during operation

\- Test parametrization and fixture refactoring



The Git history documents the incremental development process through separate test, implementation, and refactoring commits.



\## Development Highlights



\- Developed incrementally using TDD and Git-based RED-GREEN-REFACTOR workflow

\- Implemented stateful heating control with hysteresis

\- Added operating modes and manual override handling

\- Built reusable Pytest fixtures and parametrized validation tests

\- Achieved 100% statement coverage for the production controller

\- Integrated automated testing into GitHub Actions CI





