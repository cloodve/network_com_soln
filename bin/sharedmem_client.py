from multiprocessing.managers import SharedMemoryServer
import os, sys, inspect
import atexit
import time
import logging
import threading
from multiprocessing import Process
import signal

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, os.path.join(parentdir, 'client'))
sys.path.insert(0, os.path.join(parentdir, 'common'))

from shared_mem_comm.shared_server import SharedMemoryServer
from shared_mem_comm.shared_connection import SharedMemoryConnector
from sharedmem_save_msg_handler import SharedMemSaveMsgHandler
from configurations import SharedMemoryClientConfig, SharedMemoryServerConfig, DATA_FILE
from message import Message
import log

    

if __name__ == '__main__':
    stl_file = open(DATA_FILE, 'rb').read()
    stl_len = len(stl_file)

    def run_client_server():
        # time.sleep(3)
        config = SharedMemoryServerConfig()
        message_handler = SharedMemSaveMsgHandler(stl_len)
        server = SharedMemoryServer(config, message_handler)
        
        server.start()
        server.run()
        server.close()

    t = threading.Thread(target=run_client_server)
    
    t.start()
    time.sleep(3)

    logging.debug('Started listening server')

    ## Build connection to server
    shared_mem_config = SharedMemoryClientConfig()
    connection = SharedMemoryConnector(shared_mem_config)
    
    msg = Message(stl_file)

    connection.send(msg)
    connection.close()

    # time.sleep(5)
    ## Let's wait for the server to stop
    t.join()
    logging.debug('Exiting client.')
