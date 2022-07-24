from multiprocessing import shared_memory

from shared_mem_comm.shared_server import SharedMemoryLock
from base.connection import Connection
from message import Message


class SharedMemoryConnector(Connection):
    """
    Use shared memory to send messages between a client and server.
    
    """

    def __init__(self, config):
        self._config = config

    def connect(self, config): pass
        
    def send(self, msg: Message):
        self._queue =  shared_memory.SharedMemory(
            name=self._config.shared_mem_send,
            size=self._config.queue_size
        )
        self._lock = shared_memory.SharedMemory(
            name=self._config.shared_mem_send_lock,
            size=1
        )
        self._queue_size = self._config.queue_size
        with SharedMemoryLock(self._lock):
            buf = self._queue.buf
            b = msg.to_bytes()
            buf[:len(b)] = b

    def close(self): pass