import logging

logging.basicConfig(level='DEBUG', filename='mylog.log')
logger = logging.getLogger()
print(logger)
print(logger.level)
print(logger.handlers)
def main(name):
    if name not in 'mylog.log':
        logger.debug(f'Enter in the main() function: name = {name}')
        logger.debug(f'asasda: name = {name}')

if __name__ == '__main__':
    main('oleg')