import logging
import time
from xmlrpc.client import Server

from base.message_handler import BaseMessageHandler
from message import Message
from zmq_communication.zmq_connection import ZmqConnection
from configurations import ServerConnectionConfig


class ReflectMessageHandler(BaseMessageHandler):

    def handle_message(self, server, message: Message): 
        
        conf = ServerConnectionConfig()

        ip, port = conf.ip, conf.port        
        # logging.debug(f'Server is reflecting message back to client at ip {ip} and port {port}')
        
        connection = ZmqConnection()
        connection.connect(conf)

        msg_bytes = message.to_bytes()
        connection.send(message)
        connection.close()