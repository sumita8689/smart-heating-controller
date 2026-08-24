class HeatingController:
    def __init__(self,target_temp,hysteresis=0):
        self.target_temp= target_temp
        self.hysteresis = hysteresis
        self.action = "OFF"
        self.mode = "COMFORT"
    def set_mode(self,mode):
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
