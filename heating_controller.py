class HeatingController:
    def __init__(self,target_temp,hysteresis=0):
        self.target_temp= target_temp
        self.hysteresis = hysteresis
    def get_action(self,current_temp):
        if current_temp < (self.target_temp- self.hysteresis):
            return "HEATING"
        return "OFF"
