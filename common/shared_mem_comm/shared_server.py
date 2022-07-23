from multiprocessing import shared_memory
import logging
import time
import copy

from base.base_server import BaseServer
from base.message_handler import BaseMessageHandler
# from configurations import SharedMemoryConfig
from message import Message

class SharedMemoryLock:
    def __init__(self, lock):
        self._lock = lock
    
    def __enter__(self):
        # Probably could use standard library inter-process syncronization. 
        # This just seemed quick and easy.
        while self._lock.buf[0] == bytearray([1]): 
            time.sleep(0.5)

        self._lock.buf[:1] = bytearray([1])
    
    def __exit__(self, type, value, traceback):
        self._lock.buf[:1] = bytearray([0])


class SharedMemoryServer(BaseServer):
    def __init__(self, 
        config,
        processor: BaseMessageHandler):

        super().__init__(processor)

        logging.debug(f'Server listening on {config.shared_mem_send} with lock {config.shared_mem_send_lock}')
        
        self._message_handler = processor

        self._queue = shared_memory.SharedMemory(
            name=config.shared_mem_send,
            create=True, 
            size=config.queue_size
        )

        self._lock = shared_memory.SharedMemory(
            name=config.shared_mem_send_lock,
            create=True, 
            size=1
        )
        self._queue_size = config.queue_size

    def start(self): 
        # Clean out array
        with SharedMemoryLock(self._lock):
            self._queue.buf[:] = bytearray([0]*self._queue_size)

        return True

    def recv(self) -> Message:
        logging.debug('Checking for message.')

        data = bytearray([0] * self._queue_size)
        found_data = False

        # Grab lock and check if anything written
        with SharedMemoryLock(self._lock):
            if self._queue.buf[:self._queue_size] != bytearray([0]*self._queue_size):
                found_data = True
                data[:] = bytearray(self._queue.buf[:self._queue_size])
                
                
                self._queue.buf[:] = bytearray([0]*self._queue_size)

        return Message(data) if found_data else None
    
    def send(self, msg: Message): pass

    def close(self, **kwargs): pass
    
    def handle_error(self, error: Exception) -> bool: return False
        



        

