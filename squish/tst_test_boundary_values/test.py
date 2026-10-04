# -*- coding: utf-8 -*-

import names

def main():
    startApplication("SmartHeatingHMI")
    
    spinbox= waitForObject(names.temperatureGroup_targetTemperatureSpinBox_QDoubleSpinBox)
    test.compare(spinbox.minimum,20.0)
    test.compare(spinbox.maximum,30.0)
    
    spinbox.setValue(20.0)
    test.compare(spinbox.value,20.0)
    
    spinbox.setValue(30.0)
    test.compare(spinbox.value,30.0)

    spinbox.setValue(19.9)
    test.compare(spinbox.value,20.0)
    
    spinbox.setValue(30.1)
    test.compare(spinbox.value,30.0)