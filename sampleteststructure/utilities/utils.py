import inspect
import logging


class Utils():
    def __init__(self):
        self.log_level = logging.DEBUG

    def set_log_level(self, log_level):
        self.log_level = log_level

    def custom_logger(self):
        # Set to class name, helps with troubleshooting when looking at automation log
        logger_name = inspect.stack()[1][3]
        # logger creation
        logger = logging.getLogger(logger_name)
        logger.setLevel(self.log_level)
        # create handler
        file_handler = logging.FileHandler("..\\Reports\\automation.log", mode="a")
        # create formatter and add to handler
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s',
                                      datefmt="%m/%d/%Y %I:%M:%S %p")
        file_handler.setFormatter(formatter)
        # add console handler to logger
        logger.addHandler(file_handler)
        return logger
