import os
import sys
import asyncio
import queue
import threading

# local imports
from src.devices.SmartBulb import SmartBulb
from src.devices.SmartThermostat import SmartThermostat
from src.network.simulator import start_network
from src.storage.worker import file_writer_worker

async def user_command_center(devices):
    print("Control devices using <device_id> <command> <value>\nFor more info, enter 'help'")

    while True:
        # wait for input in another thread
        user_input = await asyncio.to_thread(input, "") 
        parts = user_input.split()
        if not parts: continue
        
        target_id = parts[0]
        if target_id.upper() == "HELP":
            print("""
Syntax: <device_id> <command> <value: optional>

Available commands:
    Smart Bulb:
        toggle - Turn bulb on/off
        brightness <value> - Set brightness level
        color <value> - Set color
    Smart Thermostat:
        target_temp <value> - Set target temperature
    Smart Speaker:
        toggle - Turn speaker on/off
        play <track_name> - Play a track
        pause - Pause track
        volume <value> - Set volume level
    routine <routine_name> - Activate a predefined routine
        focus - brightness 100%, thermostat 21°C
    Ctrl+C - Quit the program\n""")
            continue
        
        if len(parts) < 2:
            print("Invalid command. Try 'help' for more info.")
            continue

        action = parts[1].upper()
        value = parts[2] if len(parts) > 2 else None

        # send command to device
        found = False
        for d in devices:
            if d.device_id == target_id:
                d.execute_command(action, value)
                print(f"Command '{action}' sent to {d.name}")
                found = True
        
        if not found:
            print(f"Device {target_id} not found.")

def apply_routine(name, devices):
    print(f"Applying routine: {name}")
    if name == "FOCUS":
        for d in devices:
            if d.device_type == "BULB": d.execute_command("BRIGHTNESS", 100)
            if d.device_type == "THERMOSTAT": d.execute_command("TARGET_TEMP", 21)

async def main():
    # set up threads
    data_queue = queue.Queue()
    storage_thread = threading.Thread(
        target=file_writer_worker, 
        args=(data_queue,), 
        daemon=True
    )
    storage_thread.start()
    print("Storage thread started...")

    # initialize devices
    devices = [
        SmartBulb("b1", "Kitchen Bulb", "Kitchen"),
        SmartThermostat("t1", "Living Room Heat", "Living Room")
    ]

    # run network and device controller in parallel
    network_task = asyncio.create_task(start_network(devices, data_queue))
    ui_task = asyncio.create_task(user_command_center(devices))

    # start network simulation
    try:
        await asyncio.gather(network_task, ui_task)
    
    # ctrl+c handling
    except (asyncio.CancelledError, KeyboardInterrupt):
        pass

    except Exception as e:
        print(e)
    
    finally:
        print("\nShutting down...")
        network_task.cancel()
        data_queue.put(None)
        storage_thread.join(timeout=1)
        print("Storage saved.")
        os._exit(0) 

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        os._exit(0)