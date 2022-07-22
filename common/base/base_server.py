from abc import ABC, abstractmethod
import logging
import time

from message import Message
from base.message_handler import BaseMessageHandler
from exceptions import ServerNotStarted
import logging

class BaseServer(ABC):

    def __init__(self, processor: BaseMessageHandler):
        self._run = False
        self._message_handler = processor
        logging.debug(f'Initializing Server')

    @abstractmethod
    def start(self) -> bool: pass

    @abstractmethod
    def recv(self) -> Message: pass

    @abstractmethod
    def send(self, msg: Message) -> bool: pass

    @abstractmethod
    def close(self, **kwargs): pass

    @abstractmethod
    def handle_error(self, error: Exception) -> bool: pass

    def stop(self): 
        self._run = False
    
    def run(self): 
        logging.debug(f'Starting server {type(self)}')

        self._run = True
        import zmq
        while self._run:
            try:
                msg = self.recv()
                if msg and self._message_handler:
                    self._message_handler.handle_message(self, msg)
            except Exception as e: 
                is_handled = self.handle_error(e)
                if not is_handled:
                    logging.debug('Error:' + str(e))
                    self.stop()
                    raise e

            # Since we are blocking on receive,
            # give user chance to kill server.
            time.sleep(2)
                

