from abc import ABC, abstractmethod
import time
import asyncio
import random

class SmartDevice(ABC):
    def __init__(self, device_id, name, location):
        self.device_id = device_id
        self.name = name
        self.location = location
        self.device_type = "GENERIC"
        self.is_connected = False


    async def connect(self):
        """Simulates connecting with a random delay."""
        print(f"{self.name} is connecting...")
        start_time = time.perf_counter()
        
        # connection delay
        await asyncio.sleep(random.uniform(0.5, 2.0))
        
        end_time = time.perf_counter()
        duration = end_time - start_time
        
        self.is_connected = True
        print(f"{self.name} connected successfully in {duration:.2f}s.")

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
    def execute_command(self, command: str, *args): # accept arguments
        pass