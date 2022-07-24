

class Message: 
    """
    Very basic example of a message object. This class could go in many
    directions to provide great code reuse and functionality to the
    framework.
    """
    def __init__(self, message: bytes):
        self._msg = message
    
    def to_bytes(self) -> bytes: 
        return self._msg
    
    def to_file(self, filename: str) -> None:
        with open(filename, 'wb+') as f:
            f.write(self._msg)
