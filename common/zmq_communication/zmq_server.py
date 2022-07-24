import logging

from base.base_server import BaseServer

import zmq
from base.message_handler import BaseMessageHandler
from message import Message
from configurations import ServerConfig

class ZmqServer(BaseServer):

    def __init__(self, 
        config,
        message_handler: BaseMessageHandler):
        """
        :param message_handler: Server passes received messages to a message handler.
        """

        super().__init__(config, message_handler)
        
        self._server_config: ServerConfig = config
        self._socket: zmq.Socket = None
        
    
    def start(self) -> bool:
        port = self._server_config.port

        logging.debug(f'Starting server on port {port}')
        
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.REP)

        if hasattr(self._server_config, 'polling_timeout'):
            self._socket.setsockopt(zmq.RCVTIMEO, 
                            self._server_config.polling_timeout)
        
        self._socket.setsockopt(zmq.SNDBUF, 800000)
        self._socket.setsockopt(zmq.RCVBUF, 800000)
        
        self._socket.bind(f'tcp://*:{port}')

        return True
    
    def handle_error(self, error: Exception):
        # This code should be unnecessary, but for sake of time
        # and lack of understandig, let's put this in
        # for better user experience.
        if 'Resource temporarily unavailable' not in str(error):
            self.close(destroy=True)
        
        return True

    def recv(self) -> Message:
        logging.debug('Waiting for message.')

        msg = self._socket.recv()
        m = Message(msg)

        return m

    ## TODO: Probably not going to use this, rip it out
    ## when certain.
    def send(self, msg: bytes) -> bool: 
        self._socket.send(msg)

    def close(self, **kwargs):
        logging.debug('Closing socket.')
        self._socket.close()

        if 'destroy' in kwargs and kwargs['destroy']:
            self._context.destroy()
            self.start()