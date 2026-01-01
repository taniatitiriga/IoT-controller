# src/devices/SmartThermostat.py
from .SmartDevice import SmartDevice

class SmartThermostat(SmartDevice):
    def __init__(self, device_id, name, location):
        super().__init__(device_id, name, location)
        self.device_type = "THERMOSTAT"
        self.current_temp = 20.0
        self._target_temp = 22.0
        self.humidity = 40.0


    @property
    def target_temp(self):
        return self._target_temp

    @target_temp.setter
    def target_temp(self, value):
        # keep normal temperature range
        self._target_temp = max(15.0, min(30.0, float(value)))


    def execute_command(self, command, *args):
        if command == "TARGET_TEMP" and args:
            self.target_temp = args[0]

    def get_status(self):
        diff = self.target_temp - self.current_temp
        if diff > 0:
            self.current_temp += min(diff, 0.5)
        elif diff < 0:
            self.current_temp -= min(-diff, 0.5)

        return {
            "current_temp": self.current_temp,
            "target_temp": self.target_temp,
            "humidity": self.humidity
        }