from abc import ABC, abstractmethod
import time

class SmartDevice(ABC):
    def __init__(self, device_id, name, location):
        self.device_id = device_id
        self.name = name
        self.location = location
        self.device_type = "GENERIC"
        self.is_connected = False

    def connect(self):
        self.is_connected = True
        print(f"Device {self.name} connected")

    async def send_update(self):
        # for output formatting
        return {
            "device_id": self.device_id,
            "type": self.device_type,
            "timestamp": time.time(),
            "payload": self.get_status()
        }

    @abstractmethod
    def get_status(self) -> dict:
        pass

    @abstractmethod
    def execute_command(self, command: str):
        pass