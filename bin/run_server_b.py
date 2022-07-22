# https://github.com/Machina-Labs/network_com_hw
import os, sys, inspect
import atexit
import signal


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, os.path.join(parentdir, 'server'))
sys.path.insert(0, os.path.join(parentdir, 'common'))

from zmq_server import ZmqServer
from reflect_msg_handler import ReflectMessageHandler
from configurations import ServerConfig
import log

config = ServerConfig()
message_handler = ReflectMessageHandler()
server = ZmqServer(config, message_handler)

signal.signal(signal.SIGINT, server.stop)
atexit.register(server.close)

server.start()
server.run()



