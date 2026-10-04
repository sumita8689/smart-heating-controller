# -*- coding: utf-8 -*-

import names

source(findFile("scripts", "heating_helpers.py"))

def main():
    startApplication("SmartHeatingHMI")
    set_target_temperature(25.0)
    set_mode("COMFORT")
    apply_settings()

    target = waitForObject(names.temperatureGroup_targetTemperatureSpinBox_QDoubleSpinBox)
    mode = waitForObject(names.modeGroup_modeComboBox_QComboBox)
    test.compare(target.value, 25.0)
    test.compare(mode.currentText, "COMFORT")
    verify_status("HEATING")