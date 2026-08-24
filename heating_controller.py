class HeatingController:
    def __init__(self,target_temp,hysteresis=0):
        self.target_temp= target_temp
        self.hysteresis = hysteresis
        self.action = "OFF"
    def get_action(self,current_temp):
        if current_temp >60 or current_temp < -50:
            raise ValueError("Invalid Temperature")
        if current_temp < (self.target_temp- self.hysteresis):
            self.action = "HEATING"
        elif current_temp >= self.target_temp:
            self.action = "OFF"
        return self.action
