import asyncio
import queue
import threading

# local imports
from src.devices.SmartBulb import SmartBulb
from src.devices.SmartThermostat import SmartThermostat
from src.network.simulator import start_network
from src.storage.worker import file_writer_worker

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

    # start network simulation
    try:
        await start_network(devices, data_queue)
    
    # ctrl+c to stop
    except asyncio.CancelledError:
        pass
    
    finally:
        print("\nShutting down...")

        # signal the worker to stop
        data_queue.put(None)
        
        # wait for thread to finish
        storage_thread.join(timeout=2)
        print("Storage saved.")

if __name__ == "__main__":
    asyncio.run(main())