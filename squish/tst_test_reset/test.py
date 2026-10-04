# -*- coding: utf-8 -*-

import names


def main():
    startApplication("SmartHeatingHMI")
    
    spinbox= waitForObject(names.temperatureGroup_targetTemperatureSpinBox_QDoubleSpinBox)
    spinbox.setValue(25.0)
    
    combobox= waitForObject(names.modeGroup_modeComboBox_QComboBox)
    combobox.setCurrentText("AWAY")
    
    clickButton(waitForObject(names.controlsGroup_resetButton_QPushButton))
    
    spinbox= waitForObject(names.temperatureGroup_targetTemperatureSpinBox_QDoubleSpinBox)
    test.compare(spinbox.value,21.0)
    
    combobox= waitForObject(names.modeGroup_modeComboBox_QComboBox)
    test.compare(combobox.currentText,"COMFORT")
