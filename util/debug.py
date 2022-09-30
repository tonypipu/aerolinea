import os
import logging 
# creamos linea absoluta para el debug y configuracion basica
logging.basicConfig( level=logging.DEBUG, filename=os.path.dirname(os.path.abspath(__file__))+'/debug.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')



logger = logging.getLogger('Example_Log')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('debug.log')
fh.setLevel(logging.DEBUG)


### comandos para el log

# logger.debug('Debug Message')
# logger.info('Info Message')
# logger.warning('Warning')
# logger.error('An Error Occured')
# logger.critical('Critical error shutdown')
