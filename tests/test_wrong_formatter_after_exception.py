#!/usr/bin/env python

import logging
import sys

from cool_logging.formatters import ConsoleColorFormatter

from support_module import do_stuff

log_handler = logging.StreamHandler(sys.stderr)
log_handler.setLevel(logging.DEBUG)
log_handler.setFormatter(ConsoleColorFormatter())

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(log_handler)

logging.getLogger('support_module').setLevel(logging.DEBUG)
logging.getLogger('support_module').addHandler(log_handler)

logger.debug("Here I am")
do_stuff()
logger.debug("Here I am, again!")
