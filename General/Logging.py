import logging

# One method to use logging, comment line 7-8 if you're using the other method
# Set logging config, filename is destination file, filemode is write, log level is DEBUG and above
# Format sets the logging format, for complete list, check out official documentation
# https://docs.python.org/3/library/logging.html#formatter-objects
# logging.basicConfig(level=logging.DEBUG, filename=".\\Results\\logs.log", filemode="w",
#                     format='%(asctime)s - %(levelname)s : %(message)s', datefmt="%m/%d/%Y %I:%M:%S %p")


# Levels of logging, if set to warning then only warning and above (warning, error, critical) are recorded
# DEBUG - Detailed information, typically of interest only when diagnosing problems.
# INFO - Confirmation that things are working as expected.
# WARNING - An indication that something unexpected happened, or indicative of some problem in the near future
# (e.g. ‘disk space low’). The software is still working as expected.
# ERROR - Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL - A serious error, indicating that the program itself may be unable to continue running.

# Another method to log
def sample_logger():
    # create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # create console handler or file handler
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(".\\Results\\customlogs.log")
    # create formatter - change how logs are formatted
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s', datefmt="%m/%d/%Y %I:%M:%S %p")
    # add formatter to console or file handler
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    # add console handler to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    # application code - log messages
    logger.debug("Debug statement")
    logger.info("Info statement")
    logger.warning("Warning statement")
    logger.error("Error statement")


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return 0
    elif a == 0:
        return 0
    else:
        return a / b


sum_value = addition(5, 5)
subtraction_value = subtraction(20, 5)
multiplication_value = multiplication(10, 10)
division_value = division(10, 2)

# Takes config from line 6
# Comment lines 70-73 if using sample_logger()
# logging.debug("Debugging: result of addition is % d" % sum_value)
# logging.info("Info: result of subtraction is % d" % subtraction_value)
# logging.warning("Warning: result of multiplication is % d" % multiplication_value)
# logging.error("Error: result of division is % d" % division_value)

# second method
sample_logger()
