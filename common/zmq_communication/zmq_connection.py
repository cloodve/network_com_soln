import logging

from base.connection import Connection
from configurations import ClientConnectionConfig
from message import Message

import zmq

class ZmqConnection(Connection):
    """
    Create connection objects to servers via ZeroMQ.

    """

    def __init__(self):
        self._context = None
        self._socket = None

    def connect(self, config):
        logging.debug(f'Connecting to host - IP({config.ip}) Port({config.port})')

        ## Connection string for ZeroMQ socket.
        connection_string = f'tcp://{config.ip}:{config.port}'

        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.REQ)

        ## For simplicity, just assume we can fit the entire file into
        ## buffers.
        self._socket.setsockopt(zmq.SNDBUF, 800000)
        self._socket.setsockopt(zmq.RCVBUF, 800000)

        ## Connect ZeroMQ socket.
        self._socket.connect(connection_string)
    
    def send(self, msg: Message): 
        """ Send messages via ZeroMQ. """
        logging.debug('Sending msg.')

        serialized = msg.to_bytes()
        self._socket.send(serialized)
    
    def close(self, **kwargs):
        """ Cleanup ZeroMQ. """
        self._socket.close()
        if 'destroy' in kwargs and kwargs['destroy']:
            self._context.destroy()

    