from __future__ import annotations
from abc import ABC, abstractmethod

from message import Message

class BaseMessageHandler(ABC): 

    @abstractmethod
    def handle_message(self, server, message: Message): pass
    
        