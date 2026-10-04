# encoding: UTF-8

from objectmaphelper import *

smartHeatingHMI_QWidget = {"name": "SmartHeatingHMI", "type": "QWidget", "visible": 1}
smartHeatingHMI_modeGroup_QGroupBox = {"name": "modeGroup", "type": "QGroupBox", "visible": 1, "window": smartHeatingHMI_QWidget}
modeGroup_modeComboBox_QComboBox = {"container": smartHeatingHMI_modeGroup_QGroupBox, "name": "modeComboBox", "type": "QComboBox", "visible": 1}
smartHeatingHMI_controlsGroup_QGroupBox = {"name": "controlsGroup", "type": "QGroupBox", "visible": 1, "window": smartHeatingHMI_QWidget}
controlsGroup_applyButton_QPushButton = {"container": smartHeatingHMI_controlsGroup_QGroupBox, "name": "applyButton", "type": "QPushButton", "visible": 1}
smartHeatingHMI_statusGroup_QGroupBox = {"name": "statusGroup", "type": "QGroupBox", "visible": 1, "window": smartHeatingHMI_QWidget}
statusGroup_statusValue_QLabel = {"container": smartHeatingHMI_statusGroup_QGroupBox, "name": "statusValue", "type": "QLabel", "visible": 1}
smartHeatingHMI_temperatureGroup_QGroupBox = {"name": "temperatureGroup", "type": "QGroupBox", "visible": 1, "window": smartHeatingHMI_QWidget}
temperatureGroup_targetTemperatureSpinBox_QDoubleSpinBox = {"container": smartHeatingHMI_temperatureGroup_QGroupBox, "name": "targetTemperatureSpinBox", "type": "QDoubleSpinBox", "visible": 1}
modeGroup_modeLabel_QLabel = {"container": smartHeatingHMI_modeGroup_QGroupBox, "name": "modeLabel", "type": "QLabel", "visible": 1}
controlsGroup_resetButton_QPushButton = {"container": smartHeatingHMI_controlsGroup_QGroupBox, "name": "resetButton", "type": "QPushButton", "visible": 1}
