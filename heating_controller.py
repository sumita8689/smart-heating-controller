class HeatingController:
    def __init__(self,target_temp):
        self.target_temp= target_temp
    def get_action(self,current_temp):
        if current_temp < self.target_temp:
            return "HEATING"