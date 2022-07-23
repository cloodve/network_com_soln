import os, sys, inspect
import atexit
import signal
from multiprocessing import shared_memory


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, os.path.join(parentdir, 'server'))
sys.path.insert(0, os.path.join(parentdir, 'common'))

from shared_mem_comm.shared_server import SharedMemoryServer
from sharedmem_reflect_msg_handler import SharedMemReflectMsgHandler
from configurations import SharedMemoryServerConfig, SharedMemoryClientConfig
import log

server_config = SharedMemoryServerConfig()

message_handler = SharedMemReflectMsgHandler(server_config)

client_config = SharedMemoryClientConfig()

server = SharedMemoryServer(
    client_config,
    message_handler
)

signal.signal(signal.SIGINT, server.stop)
atexit.register(server.close)

server.start()
server.run()
