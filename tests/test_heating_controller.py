import pytest
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

def test_rejects_temperature_above_maximum():
    controller = HeatingController(target_temp=21,hysteresis=0.5)
    with pytest.raises(ValueError):
        controller.get_action(61)

def test_rejects_temperature_below_minimum():
    controller = HeatingController(target_temp=21,hysteresis=0.5)
    with pytest.raises(ValueError):
        controller.get_action(-55)

def test_off_eco_mode():
    controller = HeatingController(target_temp=21,hysteresis=0.5)
    controller.set_mode("ECO")
    result = controller.get_action(current_temp=19)
    assert result=="OFF"

def test_heating_eco_mode():
    controller = HeatingController(target_temp=21,hysteresis=0.5)
    controller.set_mode("ECO")
    result = controller.get_action(current_temp=18)
    assert result=="HEATING"

def test_switching_eco_comfort_mode():
    controller = HeatingController(target_temp=21,hysteresis=0.5)
    controller.set_mode("ECO")
    result = controller.get_action(current_temp=19)
    assert result=="OFF"
    controller.set_mode("COMFORT")
    result = controller.get_action(current_temp=19)
    assert result == "HEATING"

def test_off_away_mode():
    controller = HeatingController(target_temp=21,hysteresis=0.5)
    controller.set_mode("AWAY")
    result = controller.get_action(current_temp=16)
    assert result=="OFF"

def test_heating_away_mode():
    controller = HeatingController(target_temp=21,hysteresis=0.5)
    controller.set_mode("AWAY")
    result = controller.get_action(current_temp=15)
    assert result=="HEATING"

def test_switching_eco_away_comfort_mode():
    controller = HeatingController(target_temp=21,hysteresis=0.5)
    controller.set_mode("ECO")
    result = controller.get_action(current_temp=17)
    assert result=="HEATING"
    controller.set_mode("AWAY")
    result = controller.get_action(current_temp=19)
    assert result == "OFF"
    controller.set_mode("COMFORT")
    result = controller.get_action(current_temp=19)
    assert result == "HEATING"

def test_invalid_mode():
    controller = HeatingController(target_temp=21, hysteresis=0.5)
    with pytest.raises(ValueError):
        controller.set_mode("HOLIDAY")

def test_invalid_min_target_temperature():
    with pytest.raises(ValueError):
        HeatingController(target_temp=19, hysteresis=0.5)

def test_invalid_max_target_temperature():
    with pytest.raises(ValueError):
        HeatingController(target_temp=31, hysteresis=0.5)

def test_invalid_min_hysteresis_temperature():
    with pytest.raises(ValueError):
        HeatingController(target_temp=21, hysteresis=-1)

def test_invalid_max_hysteresis_temperature():
    with pytest.raises(ValueError):
        HeatingController(target_temp=21, hysteresis=6)

def test_target_temp_change_to_valid_value():
    controller = HeatingController(target_temp=21, hysteresis=0.5)
    controller.set_target_temperature(23)
    result = controller.get_action(22)
    assert result== ("HEATING")

def test_target_temp_change_to_invalid_value():
    controller = HeatingController(target_temp=21, hysteresis=0.5)
    with pytest.raises(ValueError):
        controller.set_target_temperature(15)

def test_activate_manual_override_on():
    controller = HeatingController(target_temp=21, hysteresis=0.5)
    controller.set_manual_override("OFF")
    result = controller.get_action(current_temp=15)
    assert result == "OFF"

def test_deactivate_manual_override_off():
    controller = HeatingController(target_temp=21, hysteresis=0.5)
    controller.set_manual_override("OFF")
    result = controller.get_action(current_temp=15)
    assert result == "OFF"
    controller.set_manual_override("AUTO")
    result = controller.get_action(current_temp=15)
    assert result == "HEATING"

def test_activate_manual_override_invalid():
    controller = HeatingController(target_temp=21, hysteresis=0.5)
    with pytest.raises(ValueError):
        controller.set_manual_override("ABC")

def test_targettemp_change_manualoverride_on_mode():
    controller = HeatingController(target_temp=21, hysteresis=0.5)
    controller.set_manual_override("OFF")
    controller.set_target_temperature(27)
    result = controller.get_action(current_temp=15)
    assert result=="OFF"

def test_mode_manualoverride_independence():
    controller = HeatingController(target_temp=21, hysteresis=0.5)
    controller.set_manual_override("OFF")
    controller.set_mode("AWAY")
    result = controller.get_action(current_temp=10)
    assert result=="OFF"

def test_new_controller_without_manualoverride_active():
    controller = HeatingController(target_temp=21, hysteresis=0.5)
    controller.set_manual_override("OFF")
    result = controller.get_action(current_temp=10)
    assert result=="OFF"
    controller2 = HeatingController(target_temp=21, hysteresis=0.5)
    result = controller2.get_action(current_temp=10)
    assert result=="HEATING"

def test_manualoverride_state_switch():
    controller = HeatingController(target_temp=21, hysteresis=0.5)
    controller.set_manual_override("OFF")
    result = controller.get_action(current_temp=10)
    assert result=="OFF"
    controller.set_manual_override("AUTO")
    result = controller.get_action(current_temp=10)
    assert result=="HEATING"
    controller.set_manual_override("OFF")
    result = controller.get_action(current_temp=10)
    assert result=="OFF"
    controller.set_manual_override("AUTO")
    result = controller.get_action(current_temp=10)
    assert result=="HEATING"

def test_targettemp_change_auto_mode():
    controller = HeatingController(target_temp=21, hysteresis=0.5)
    result = controller.get_action(current_temp=22)
    assert result=="OFF"
    controller.set_target_temperature(23)
    result = controller.get_action(current_temp=22)
    assert result=="HEATING"

def test_targettemp_change_eco_mode():
    controller = HeatingController(target_temp=21, hysteresis=0.5)
    controller.set_mode("ECO")
    result = controller.get_action(current_temp=18)
    assert result=="HEATING"
    controller.set_target_temperature(20)
    result = controller.get_action(current_temp=20)
    assert result=="OFF"


def test_targettemp_change_away_mode():
    controller = HeatingController(target_temp=20, hysteresis=0.5)
    controller.set_mode("AWAY")
    result = controller.get_action(current_temp=14)
    assert result == "HEATING"
    controller.set_target_temperature(21)
    result = controller.get_action(current_temp=16)
    assert result == "OFF"

def test_targettemp_change_auto_mode_while_heating_on():
    controller = HeatingController(target_temp=21, hysteresis=0.5)
    result = controller.get_action(current_temp=20)
    assert result=="HEATING"
    controller.set_target_temperature(23)
    result = controller.get_action(current_temp=20)
    assert result=="HEATING"

def test_targettemp_change_auto_mode_heatingon_to_off():
    controller = HeatingController(target_temp=21, hysteresis=0.5)
    result = controller.get_action(current_temp=20)
    assert result=="HEATING"
    controller.set_target_temperature(20)
    result = controller.get_action(current_temp=20)
    assert result=="OFF"