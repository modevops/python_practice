import logging
import warning

logging.basicConfig(level=logging.INFO,)
warning.warn('This warning is not sent to the logs')
logging.captureWarning(True)
warning.warn('This warning is sent to the logs')