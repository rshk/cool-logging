Cool Logging
############

A cool formatter for colored logging output.

It uses ``termcolor`` to colorize the output of the standard Python
logging module.


Installation
============

Simply::

    $ pip install cool_logging


Or, for the development version::

    $ pip install -e git+git@github.com:rshk/cool-logging.git#egg=cool_logging


Example usage
=============

No more remembering to add handlers, formatters, etc. etc.!

Now you do::

    from cool_logging import getLogger
    logger = getLogger(__name__)

and start logging right away!
