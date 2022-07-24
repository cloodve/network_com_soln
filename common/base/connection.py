from abc import ABC, abstractmethod

from configurations import ClientConnectionConfig
from message import Message


class Connection(ABC):
    """ 
    Abstract base class. A better name may exist for this functionality. 
    The idea is to connect to a server and send messages.

    """

    @abstractmethod
    def connect(self, config): pass
    """ Initialize a connection to server. """

    @abstractmethod
    def send(self, msg: Message): pass
    """ Send messages to the server. """

    @abstractmethod
    def close(self): pass
    """ close any application or OS handles. """
    
    