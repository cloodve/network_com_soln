import logging

from base.connection import Connection
from configurations import ClientConnectionConfig
from message import Message

import zmq

class ZmqConnection(Connection):

    def __init__(self):
        self._context = None
        self._socket = None

    def connect(self, config):
        logging.debug(f'Connecting to host - IP({config.ip}) Port({config.port})')

        connection_string = f'tcp://{config.ip}:{config.port}'

        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.REQ)
        self._socket.setsockopt(zmq.SNDBUF, 800000)
        self._socket.setsockopt(zmq.RCVBUF, 800000)
        self._socket.connect(connection_string)
    
    def send(self, msg: Message): 
        logging.debug('Sending msg.')
        serialized = msg.to_bytes()
        # logging.debug('Sending: ', str(serialized)[0:10])
        self._socket.send(serialized)
    
    def close(self, **kwargs):
        self._socket.close()
        if 'destroy' in kwargs and kwargs['destroy']:
            self._context.destroy()

    