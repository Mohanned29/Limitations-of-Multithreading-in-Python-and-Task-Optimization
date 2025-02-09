import logging
from .config import Config

def get_logger(name: str = "SmartExecutor") -> logging.Logger:
    """
    retourne un logger configure pour SmartExecutor
    Ce logger envoie les messages à la fois à la console et dans un fichier.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(Config.LOG_LEVEL)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        ch = logging.StreamHandler()
        ch.setLevel(Config.LOG_LEVEL)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        fh = logging.FileHandler(Config.LOG_FILE)
        fh.setLevel(Config.LOG_LEVEL)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
