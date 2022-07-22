from abc import ABC, abstractmethod

from configurations import ClientConnectionConfig
from message import Message


class Connection(ABC):

    @abstractmethod
    def connect(self, config): pass

    @abstractmethod
    def send(self, msg: Message): pass

    @abstractmethod
    def close(self): pass
    
    