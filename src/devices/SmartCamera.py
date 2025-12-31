import time
from .SmartDevice import SmartDevice

class SmartCamera(SmartDevice):
    def __init__(self, device_id, name, location):
        super().__init__(device_id, name, location)
        self.device_type = "CAMERA"
        self.motion_detected = False
        self._battery_level = 100
        self.last_snapshot = time.time()

    @property
    def battery_level(self):
        return self._battery_level
    
    @battery_level.setter
    def battery_level(self, value):
        self._battery_level = max(0, min(100, value))

    def get_status(self):
        self.battery_level -= 0.1 # simulate battery
        return {
            "motion_detected": self.motion_detected,
            "last_snapshot": self.last_snapshot,
            "battery_level": self.battery_level
        }

    def execute_command(self, command):
        if command == "SNAP": self.last_snapshot = time.time()