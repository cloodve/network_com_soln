import logging

from base.message_handler import BaseMessageHandler
from message import Message

from configurations import SAVE_DATA_FILE

class SharedMemSaveMsgHandler(BaseMessageHandler):
    """
    Message handler to store messages received from the server
    and save those messages to file.
    """
    def __init__(self, file_length):
        self._filelength = file_length

    def handle_message(self, server, message: Message):
        logging.debug(f'Saving file to {SAVE_DATA_FILE}')
        
        msg = Message(message.to_bytes()[:self._filelength])
        logging.debug(f'Saving file with bytes: {msg.to_bytes()[:100]}')
        f = msg.to_file(SAVE_DATA_FILE)

        server.stop()