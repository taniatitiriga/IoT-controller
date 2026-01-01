from .SmartDevice import SmartDevice

class SmartSpeaker(SmartDevice):
    def __init__(self, device_id, name, location):
        super().__init__(device_id, name, location)
        self.device_type = "SPEAKER"
        self._volume = 50 
        self.current_track = None  # None = no song playing
        self.is_on = True


    @property
    def volume(self):
        return self._volume

    @volume.setter
    # volume in range 0-100
    def volume(self, value):
        try:
            numeric_value = int(value)
            self._volume = max(0, min(100, numeric_value))
        except (ValueError, TypeError):
            print(f"Error: Invalid volume value '{value}'")


    def execute_command(self, command, *args):
        command = command.upper()
        
        if command == "PLAY" and args:
            self.current_track = " ".join(args) # for longer track names
            print(f"[{self.name}] Now playing: {self.current_track}")
            
        elif command == "PAUSE":
            self.current_track = None
            print(f"[{self.name}] Track paused.")
            
        elif command == "VOLUME" and args:
            # triggers @volume.setter
            self.volume = args[0]
            
        elif command == "TOGGLE":
            self.is_on = not self.is_on

    def get_status(self):
        return {
            "is_on": self.is_on,
            "volume": self.volume,
            "current_track": self.current_track or "IDLE"
        }