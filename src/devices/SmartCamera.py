# src/devices/SmartCamera.py
from .SmartDevice import SmartDevice
import time

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
        # battery range 0-100
        self._battery_level = max(0, min(100, value))


    def execute_command(self, command, *args):
        if command == "SNAP":
            self.last_snapshot = time.time()

    def get_status(self):
        return {
            "motion_detected": self.motion_detected,
            "battery_level": self.battery_level,
            "last_snapshot": self.last_snapshot
        }