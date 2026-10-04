# -*- coding: utf-8 -*-

import names
source(findFile("scripts", "heating_helpers.py"))

def is_heating():
    status= waitForObject(names.statusGroup_statusValue_QLabel)
    return status.text == "HEATING"

def main():
    startApplication("SmartHeatingHMI")
    set_target_temperature(25.0)
    apply_settings()
    waitFor(is_heating,5000)
    verify_status("HEATING")
