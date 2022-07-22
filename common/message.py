

class Message: 
    def __init__(self, message):
        self._msg = message
    
    def to_bytes(self) -> bytes: 
        return self._msg
    
    def to_file(self, filename: str):
        
        with open(filename, 'wb+') as f:
            f.write(self._msg)
