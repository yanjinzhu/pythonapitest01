import logging
from logging import handlers

HOST = "http://192.168.1.160:5000"
HEADERS = {"Content-Type":"application/json"}

class InitLog():
    fmt = "%(asctime)s %(levelname)s [ %(filename)s %(funcName)s %(lineno)d ] - [ %(message)s ]"

    formatter = logging.Formatter(fmt)

    sh = logging.StreamHandler()
    fh = logging.handlers.TimedRotatingFileHandler("./log/yuze.log", when="D", backupCount=7, interval=1, encoding="utf-8")

    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(sh)
    logger.addHandler(fh)

    logger.setLevel(logging.INFO)
