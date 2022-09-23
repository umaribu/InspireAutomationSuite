import logging


class LogGen:
    @staticmethod
    def logs():

        logger = logging.getLogger()
        filehandler = logging.FileHandler("C:/Users/umari/PycharmProjects/InspireAutomation/src/Logs/logfile.log")
        formatter = logging.Formatter("%(asctime)s: %(message)s: %(name)s: ", datefmt="%Y-%m-%d  %H:%M:%S")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger
