import logging

class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:/Users/mumu/PycharmProjects/PytestFrameworkScratch/Logs/automation.log",
                            format= '%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%H %p')


        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger