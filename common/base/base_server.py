from abc import ABC, abstractmethod
import logging
import time

from message import Message
from base.message_handler import BaseMessageHandler
from exceptions import ServerNotStarted
import logging

class BaseServer(ABC):
    """
    Abstract base class to setup servers. These servers are used by
    the framework to receive data and pass messages along to the message
    handlers. 

    """

    def __init__(self, config, handler: BaseMessageHandler):
        logging.debug(f'Initializing Server')

        self._run = False
        self._message_handler = handler

    @abstractmethod
    def start(self) -> bool: pass
    """ Allows client to initialize server. """

    @abstractmethod
    def recv(self) -> Message: pass
    """ Client will read in messages. Provides great flexibility
        for different types of connectivity.    
    """

    @abstractmethod
    def send(self, msg: Message) -> bool: pass
    """ Currently not used. But could allow for using the 
        same object for sending that is used for receiving.  """

    @abstractmethod
    def close(self, **kwargs): pass
    """ Close any type of application or OS handles. """

    @abstractmethod
    def handle_error(self, error: Exception) -> bool: pass
    """ Server will catch all errors, and allow the 
        client to handle. This allows the server
        to be a completely generic object.
    """

    def stop(self): 
        """ Stop the main loop from running. This mechanism works
            but there are several flaws with it.  """
        self._run = False
    
    def run(self): 
        """ Main run loop. """
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
