import logging

from base.message_handler import BaseMessageHandler
from message import Message

from configurations import SAVE_DATA_FILE

class SaveMsgHandler(BaseMessageHandler):
    """
    A message handler for the client to store message received from
    the server to the file.
    
    """

    def handle_message(self, server, message: Message):
        logging.debug(f'Saving file to {SAVE_DATA_FILE}')
        f = message.to_file(SAVE_DATA_FILE)
        server.stop()
        