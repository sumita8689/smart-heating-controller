from heating_controller import HeatingController

def test_heating_when_temp_below_target_temp():
    controller = HeatingController(target_temp=21)
    result = controller.get_action(current_temp=19)
    assert result == 'HEATING'

def test_off_when_temp_greaterorequalto_target_temp():
    controller = HeatingController(target_temp=22)
    result = controller .get_action(current_temp=22)
    assert result == "OFF"

def test_heating_when_temp_below_lower_hysteresis_limit():
    controller = HeatingController(target_temp=21,hysteresis=0.5)
    result = controller.get_action(current_temp=20.3)
    assert result == "HEATING"

def test_heating_remains_on_within_hysteresis_range():
    controller = HeatingController(target_temp=21,hysteresis=0.5)
    controller.get_action(current_temp=20.3)
    result = controller.get_action(current_temp=20.7)
    assert result == "HEATING"