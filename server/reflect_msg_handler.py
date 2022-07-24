import logging
import time
# from xmlrpc.client import Server

from base.message_handler import BaseMessageHandler
from message import Message
from zmq_communication.zmq_connection import ZmqConnection
from configurations import ServerConnectionConfig


class ReflectMessageHandler(BaseMessageHandler):
    """
    Message handler ot send ZeroMQ based messages back to the client.

    """

    def handle_message(self, server, message: Message): 
        logging.debug('Received message from client, reflecting to server.')
        
        conf = ServerConnectionConfig()

        ip, port = conf.ip, conf.port        
        
        connection = ZmqConnection()
        connection.connect(conf)
        
        connection.send(message)
        connection.close()