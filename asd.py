import logging

logging.basicConfig(filename='example.log', encoding='UTF-8', format= '%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', level='DEBUG')
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')