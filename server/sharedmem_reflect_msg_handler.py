from multiprocessing import shared_memory
import logging

from base.message_handler import BaseMessageHandler
from shared_mem_comm.shared_connection import SharedMemoryConnector
from message import Message



class SharedMemReflectMsgHandler(BaseMessageHandler):
    
    def __init__(self, config):
        self._config = config

    def handle_message(self, server, message: Message):

        logging.debug('Reflecting data back')
        conn = SharedMemoryConnector(self._config)
        conn.send(message)
        
        


