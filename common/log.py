import logging
import sys

# FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
# FORMAT = '%(asctime)s -8s %(message)s'
FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

logging.basicConfig(format=FORMAT, encoding='utf-8', level=logging.DEBUG)
