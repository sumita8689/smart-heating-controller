# -*- coding: utf-8 -*-

import names

def set_target_temperature(temperature):
    spinbox= waitForObject(names.temperatureGroup_targetTemperatureSpinBox_QDoubleSpinBox)
    spinbox.setValue(temperature)

def set_mode(mode):
    mode_combo = waitForObject(names.modeGroup_modeComboBox_QComboBox)
    mode_combo.setCurrentText(mode)
    
def apply_settings():
    clickButton(waitForObject(names.controlsGroup_applyButton_QPushButton))
    
def verify_status(expected_status):
    def status_is_correct():
        status = waitForObject(names.statusGroup_statusValue_QLabel)
        return status.text == expected_status
    
    result=waitFor(status_is_correct, 5000)
    
    test.verify(result,"Expected status: " + expected_status)
