from heating_controller import HeatingController
import pytest

@pytest.fixture
def controller(scope="function"):
    return HeatingController(target_temp=21,hysteresis=0.5)