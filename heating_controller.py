class HeatingController:
    def __init__(self,target_temp,hysteresis=0):
        self.validate_target_temp(target_temp)
        self.target_temp= target_temp
        if hysteresis< 0 or hysteresis> 5:
            raise ValueError("hysteresis temperature value outside range")
        self.hysteresis = hysteresis
        self.action = "OFF"
        self.mode = "COMFORT"
        self.manual = False

    def validate_target_temp(self,targettemp):
        if targettemp <20 or targettemp >30:
            raise ValueError("target temperature value outside range")
        return True

    def set_target_temperature(self,newtemp):
        self.validate_target_temp(newtemp)
        self.target_temp = newtemp

    def set_mode(self,mode):
        if mode not in ["ECO","COMFORT","AWAY"]:
            raise ValueError("Invalid mode")
        self.mode =mode

    def set_manual_override(self,override):
        if override not in ["OFF","AUTO"]:
            raise ValueError("Invalid mode")
        if override == "OFF":
            self.manual = True
        elif override == "AUTO":
            self.manual = False

    def get_action(self,current_temp):
        if current_temp >60 or current_temp < -50:
            raise ValueError("Invalid Temperature")
        effective_target = self.target_temp
        if self.mode == "ECO":
            effective_target = self.target_temp -2
        elif self.mode == "AWAY":
            effective_target = self.target_temp -5
        if self.manual:
            self.action = "OFF"
        else:
            if current_temp < (effective_target- self.hysteresis):
                self.action = "HEATING"
            elif current_temp >= effective_target:
                self.action = "OFF"
        return self.action
