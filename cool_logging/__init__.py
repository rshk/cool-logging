"""
:author: samu
:created: 2/20/13 7:07 PM
"""

__version__ = '0.1-beta'


def getLogger(name=None, level=None, handler=None):
    """
    Utility function, since I'm lazy :)
    """
    import logging
    import sys
    from cool_logging.formatters import ConsoleColorFormatter

    logger = logging.getLogger(name)

    if level is None:
        level = logging.DEBUG
    logger.setLevel(level)

    if handler is None:
        handler = logging.StreamHandler(sys.stderr)
        handler.setFormatter(ConsoleColorFormatter())

    if not isinstance(handler, (list, tuple)):
        handler = [handler]

    for h in handler:
        logger.addHandler(h)

    return logger
