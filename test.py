import logging
import psutil
logging.basicConfig(filename='test.log', format ='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level='DEBUG')
logging.debug('is when this event was logged.')