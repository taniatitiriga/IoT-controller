from .SmartDevice import SmartDevice

class SmartBulb(SmartDevice):
    def __init__(self, device_id, name, location):
        super().__init__(device_id, name, location)
        self.device_type = "BULB"
        self.is_on = False
        self._brightness = 100

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        # valid values check
        self._brightness = max(0, min(100, value))

    def get_status(self):
        return {"is_on": self.is_on, "brightness": self.brightness}

    def execute_command(self, command):
        if command == "TOGGLE": self.is_on = not self.is_on