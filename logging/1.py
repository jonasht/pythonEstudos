import logging

logging.basicConfig(filename='teste.log', level=logging.DEBUG)
for i in range(10):
    logging.warn(i)
    
for i in range(12):
    logging.debug(i)
    logging.error(i)