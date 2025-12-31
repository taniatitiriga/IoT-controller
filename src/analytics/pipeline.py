from dataclasses import dataclass
from functools import reduce

@dataclass
class DeviceReading:
    device_id: str
    device_type: str
    value: float # standard for temp, battery

def run_analytics(raw_updates):

    # mapping
    readings = list(map(lambda x: DeviceReading(
        x['device_id'], 
        x['type'], 
        x['payload'].get('current_temp', x['payload'].get('battery_level', 0))
    ), raw_updates))

    # filtering
    critical = list(filter(lambda r: r.device_type == "THERMOSTAT" and r.value > 25, readings))

    # compute temperature
    thermos = list(filter(lambda r: r.device_type == "THERMOSTAT", readings))
    if thermos:
        avg_temp = reduce(lambda acc, r: acc + r.value, thermos, 0) / len(thermos)
        print(f"Analytics: Average House Temp: {avg_temp:.2f}°C")