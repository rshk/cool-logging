import logging

logger = logging.getLogger(__name__)


def do_stuff():
    logger.debug("Yay, this works")
    try:
        raise ValueError("Yay")
    except:
        logger.exception("Oooops...")
    logger.debug("This is other stuff")
    logger.info("This is other stuff....")
