import os, inspect
from dataclasses import dataclass

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
# sys.path.insert(0, os.path.join(parentdir, 'data'))

## Data File Name
FILE_NAME = 'cad_mesh.stl'
DATA_FILE = os.path.join(parentdir, 'data', FILE_NAME)

SAVE_FILE_NAME = 'output.stl'
SAVE_DATA_FILE = os.path.join(parentdir, 'data', SAVE_FILE_NAME)

@dataclass
class ServerConfig:
    port = 5555
    polling_timeout = 5000

@dataclass
class ServerConnectionConfig:
    port = 5556
    ip = '127.0.0.1'

@dataclass
class ClientConfig:
    port = 5556
    polling_timeout = 5000

@dataclass
class ClientConnectionConfig:
    ip = '127.0.0.1'
    port = 5555