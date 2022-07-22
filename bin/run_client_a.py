# https://github.com/Machina-Labs/network_com_hw
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

from zmq_communication.zmq_server import ZmqServer
from zmq_communication.zmq_connection import ZmqConnection
from save_msg_handler import SaveMsgHandler
from configurations import ClientConfig, ClientConnectionConfig, DATA_FILE
from message import Message
import log



if __name__ == '__main__':
    def run_client_server():
        # time.sleep(3)
        config = ClientConfig()
        message_handler = SaveMsgHandler()
        server = ZmqServer(config, message_handler)
        
        server.start()
        server.run()
        server.close()

    t = threading.Thread(target=run_client_server)
    
    t.start()
    time.sleep(3)

    # if server:
    #     signal.signal(signal.SIGINT, server.stop)
    #     atexit.register(server.close)

    logging.debug('Started listening server')

    ## Build connection to server
    client_connection_config = ClientConnectionConfig()
    connection = ZmqConnection()
    connection.connect(client_connection_config)

    stl_file = open(DATA_FILE, 'rb').read()
    # print(stl_file)
    msg = Message(stl_file)

    connection.send(msg)
    connection.close()

    # time.sleep(5)
    ## Let's wait for the server to stop
    t.join()
    logging.debug('Exiting client.')

