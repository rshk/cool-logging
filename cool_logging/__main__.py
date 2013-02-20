#!/usr/bin/env python

if __name__ == '__main__':
    from cool_logging import getLogger
    logger = getLogger('testing')

    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warn("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

    logger.debug("This is a debug message, with a quite long text that "
                 "will certainly exceed the 70 columns limit allowed "
                 "by the custom formatter.\n"
                 "This is another line of text, at last..")
