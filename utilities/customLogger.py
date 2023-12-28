import logging
from secrets import randbelow


class LogGenerations:
    path = "C:\\Users\\zaman\\PycharmProjects\\PythonSelenium\\Logs\\"

    @staticmethod
    def logGen():
        logging.basicConfig(filename=LogGenerations.path + "automation_" + str(randbelow(50)) + "_.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger
