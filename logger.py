import logging
logger = logging.getLogger('me')
logging.basicConfig(format ='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('%s before you %s', 'Look', 'leap!')