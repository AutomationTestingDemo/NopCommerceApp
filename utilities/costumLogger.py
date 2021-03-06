import logging
import os
class LogGen:
    @staticmethod
    def loggen():
        # for handler in logging.root.handlers[:]:
        #     logging.root.removeHandler(handler)
        logging.basicConfig(filename=".\\logs\\automation.log", format="%(asctime)s:%(levelname)s:%(message)s",
                            datefmt='%m/%d/%y %I:%M:%s %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger