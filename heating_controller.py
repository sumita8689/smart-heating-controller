class HeatingController:
    def __init__(self,target_temp,hysteresis=0):
        if target_temp < 20 or target_temp > 30:
            raise ValueError("target temperature value outside range")
        self.target_temp= target_temp
        if hysteresis< 0 or hysteresis> 5:
            raise ValueError("hysteresis temperature value outside range")
        self.hysteresis = hysteresis
        self.action = "OFF"
        self.mode = "COMFORT"
    def set_mode(self,mode):
        if mode not in ["ECO","COMFORT","AWAY"]:
            raise ValueError("Invalid mode")
        self.mode =mode
    def get_action(self,current_temp):
        if current_temp >60 or current_temp < -50:
            raise ValueError("Invalid Temperature")
        effective_target = self.target_temp
        if self.mode == "ECO":
            effective_target = self.target_temp -2
        elif self.mode == "AWAY":
            effective_target = self.target_temp -5
        if current_temp < (effective_target- self.hysteresis):
            self.action = "HEATING"
        elif current_temp >= effective_target:
            self.action = "OFF"
        return self.action
