from __future__ import annotations
from abc import ABC, abstractmethod

from message import Message

class BaseMessageHandler(ABC): 
    """
    Server calls the message handler. When messages come in 
    clients of this class process an inboumd message.

    """

    @abstractmethod
    def handle_message(self, server, message: Message): pass
    
        