import logging
import sys

## Configure and setup basic logging for the application.
FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

## In this simplified framework, only use debug. When productionalizing,
## it would be desirable to use different logging levels for different
## phases of the code lifecycle (i.e. development, test, performance test, production).
logging.basicConfig(format=FORMAT, encoding='utf-8', level=logging.DEBUG)
