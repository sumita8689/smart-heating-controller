# -*- coding: utf-8 -*-

import names

def main():
    startApplication("SmartHeatingHMI")

    status = waitForObject(names.statusGroup_statusValue_QLabel)

    # Wait until the backend status reaches the HMI.Ensure docker, subscriber and publisher are running
    waitFor(lambda: status.text == "HEATING",5000)

    test.compare(status.text, "HEATING")
