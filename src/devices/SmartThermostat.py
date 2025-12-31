import random
from .SmartDevice import SmartDevice

class SmartThermostat(SmartDevice):
    def __init__(self, device_id, name, location):
        super().__init__(device_id, name, location)
        self.device_type = "THERMOSTAT"
        self.current_temp = 20.0
        self.target_temp = 24.0
        self.humidity = 40.0

    def get_status(self):
        # simulate temperature variation
        self.current_temp += random.uniform(-0.5, 0.5)
        return {
            "current_temp": self.current_temp,
            "target_temp": self.target_temp, 
            "humidity": self.humidity
        }

    def execute_command(self, command):
        if command == "BOOST": self.target_temp += 2