import threading
import json

def file_writer_worker(data_queue):
    """Pulls from queue and writes to disk."""
    with open("history.log", "a") as f:
        while True:
            data = data_queue.get()
            if data is None:
                break  # stop

            f.write(json.dumps(data) + "\n")
            f.flush() # write to disk
            data_queue.task_done()
