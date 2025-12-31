import asyncio
import random

async def simulate_device_stream(device, data_queue):
    """
    Simulate data packets from a smart device.
    """
    while True:
        # simulate random inputs
        await asyncio.sleep(random.uniform(1, 3))
        
        # get data from device
        update = await device.send_update()
        
        # dump data to queue
        data_queue.put(update)
        print(f"Network: {device.name} sent packet.")

async def start_network(devices, data_queue):
    """
    Manage concurrent connections with asyncio.
    """

    print("Connecting devices...")
    await asyncio.gather(*(d.connect() for d in devices))
    print("All devices connected!")

    tasks = [asyncio.create_task(simulate_device_stream(d, data_queue)) for d in devices]
    await asyncio.gather(*tasks)