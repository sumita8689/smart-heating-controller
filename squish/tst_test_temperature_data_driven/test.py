# -*- coding: utf-8 -*-

import names
source(findFile("scripts", "heating_helpers.py"))

def main():
    startApplication("SmartHeatingHMI")
    
    dataset = testData.dataset("temperature_data.csv")
    for record in dataset:
        temperature = testData.field(record, "target_temperature")
        expected= testData.field(record, "expected_status")
        set_target_temperature(float(temperature))
        apply_settings()
        verify_status(expected)