import logging


from base.base_server import BaseServer

import zmq
from base.message_handler import BaseMessageHandler
from message import Message
from configurations import ServerConfig

class ZmqServer(BaseServer):

    def __init__(self, 
        server_config: ServerConfig, 
        message_handler: BaseMessageHandler):

        super().__init__(message_handler)
        self._context = zmq.Context()

        self._server_config: ServerConfig = server_config
        self._socket: zmq.Socket = None
        
    
    def start(self) -> bool:
        port = self._server_config.port

        logging.debug(f'Starting server on port {port}')

        self._socket = self._context.socket(zmq.REP)

        if hasattr(self._server_config, 'polling_timeout'):
            self._socket.setsockopt(zmq.RCVTIMEO, 
                            self._server_config.polling_timeout)
        
        self._socket.setsockopt(zmq.SNDBUF, 800000)
        self._socket.setsockopt(zmq.RCVBUF, 800000)
        
        self._socket.bind(f'tcp://*:{port}')

        return True

    def recv(self) -> Message:
        logging.debug('Waiting for message.')

        msg = self._socket.recv()
        m = Message(msg)

        return m

    def send(self, msg: bytes) -> bool: 
        self._socket.send(msg)

    def close(self):
        logging.debug('Closing socket.')
        self._socket.close()