from .SmartDevice import SmartDevice

class SmartBulb(SmartDevice):
    def __init__(self, device_id, name, location):
        super().__init__(device_id, name, location)
        self.device_type = "BULB"
        self.is_on = False
        self._brightness = 100
        self.color_temp = 2700 # Kelvin


    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        try:
            numeric_val = int(float(value))
            self._brightness = max(0, min(100, numeric_val))
        except ValueError:
            print(f"\n[Error] Invalid brightness: '{value}', expected number 0-100.")
    
    
    @property
    def color_temp(self):
        return self._color_temp

    @color_temp.setter
    def color_temp(self, value):
        try:
            clean_val = str(value).rstrip('Kk')
            numeric_val = int(float(clean_val))
            self._color_temp = max(2000, min(7000, numeric_val))
        except ValueError:
            print(f"\n[Error] Invalid color: '{value}', expected number 2000-7000.")


    def execute_command(self, command, *args):
        if command == "TOGGLE": self.is_on = not self.is_on
        elif command == "BRIGHTNESS" and args: self.brightness = int(args[0])
        elif command == "COLOR" and args: self.color_temp = int(args[0])

    def get_status(self):
         return {"is_on": self.is_on, "brightness": self.brightness, "color_temp": self.color_temp}
