from dataclasses import dataclass

@dataclass(frozen=True) # immutability
class DeviceReading:
    device_id: str
    device_type: str
    timestamp: float
    value: float