"""Queue module for IoT device management."""
import queue

class DeviceQueue:
    def __init__(self):
        self._queue = queue.Queue()
    
    def enqueue(self, device):
        self._queue.put(device)
    
    def dequeue(self):
        return self._queue.get() if not self._queue.empty() else None
