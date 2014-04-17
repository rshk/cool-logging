#!/usr/bin/env python
# coding=utf-8

if __name__ == '__main__':
    import logging
    import sys
    from cool_logging.formatters import ConsoleColorFormatter, SimpleColorLog

    logger = logging.getLogger('test')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stderr)
    logger.addHandler(handler)
    formatters = [
        ConsoleColorFormatter(),
        SimpleColorLog()
    ]

    for formatter in formatters:
        handler.setFormatter(formatter)

        logger.debug("Showing formatter: {0!r}".format(formatter))

        logger.debug("This is a debug message")
        logger.info("This is an info message")
        logger.warn("This is a warning message")
        logger.error("This is an error message")
        logger.critical("This is a critical message")

        logger.debug("This is a debug message, with a quite long text that "
                     "will certainly exceed the 70 columns limit allowed "
                     "by the custom formatter.\n"
                     "This is another line of text, at last..")

        logger.debug(u"Øk, ñøw let's try with sömë utf8 cháráctérß..")
        logger.debug(u"\xd8k, \xf1\xf8w let's try with s\xf6m\xeb utf8 "
                     u"ch\xe1r\xe1ct\xe9r\xdf..")
