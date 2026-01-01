import asyncio
import random
import time

async def simulate_device_stream(device, data_queue):
    """
    Simulate data packets from a smart device.
    """
    last_packet_time = time.time()

    while True:
        # simulate random inputs
        await asyncio.sleep(random.uniform(1, 12))
        
        # get data from device
        update = await device.send_update()
        data_queue.put(update)

        current_time = time.time()
        if current_time - last_packet_time > 10:
            print(f"\n{device.name} last response: {time.time() - last_packet_time:.1f}s ago")
            
        last_packet_time = time.time()

async def start_network(devices, data_queue):
    print("Connecting devices...")
    await asyncio.gather(*(d.connect() for d in devices))
    print("All devices connected!\n")

    tasks = [asyncio.create_task(simulate_device_stream(d, data_queue)) for d in devices]
    await asyncio.gather(*tasks)