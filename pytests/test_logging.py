import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # filehandler object

    logger.setLevel(logging.DEBUG)
    logger.debug("debug statement is executed")
    logger.info("information statement is executed")
    logger.warning("warning statement is executed")
    logger.error("error statement is executed")
    logger.critical("critical statement is executed")

