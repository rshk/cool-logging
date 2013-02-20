"""
:author: samu
:created: 2/20/13 7:11 PM
"""

import logging

from termcolor import colored


LOG_FORMAT_CONSOLE_COLOR = \
    "%(c_date)s %(c_leveltag)s %(c_name)s %(c_function)s\n%(indented_message)s"
LOG_DATEFMT_CONSOLE_COLOR = "%F %T"


def _colorer(*args, **kwargs):
    return lambda x: colored(x, *args, **kwargs)


class LazyRecordColorer(object):
    colorers = {
        logging.DEBUG: _colorer('cyan', 'on_blue', attrs=['bold']),
        logging.INFO: _colorer('yellow', 'on_green', attrs=['bold']),
        logging.WARNING: _colorer('white', 'on_yellow', attrs=['bold']),
        logging.ERROR: _colorer('white', 'on_red', attrs=['bold']),
        logging.CRITICAL: _colorer('yellow', 'on_red', attrs=['bold']),
    }

    leveltags = {
        logging.DEBUG: "DBG>",
        logging.INFO: "INFO",
        logging.WARNING: "WARN",
        logging.ERROR: "ERR!",
        logging.CRITICAL: "CRIT",
    }

    def __init__(self, record):
        self.record = record

    def __getitem__(self, item):
        method = 'get_%s' % item
        if hasattr(self, method):
            return getattr(self, method)()
        return self.record.__dict__[item]

    def get_c_date(self):
        return colored('%(asctime)s,%(msecs)03d' % self.record.__dict__, 'cyan')

    def get_c_asctime(self):
        return colored(self.record.asctime, 'cyan')

    def get_c_leveltag(self):
        colorer = self.colorers.get(self.record.levelno, lambda x: x)
        return colorer(' %s ' % self.leveltags.get(self.record.levelno, '????'))

    def get_c_levelname(self):
        colorer = self.colorers.get(self.record.levelno, lambda x: x)
        return colorer(' %s ' % self.record.levelname)

    def get_c_name(self):
        return colored('[%s]' % self.record.name, 'yellow', attrs=['bold'])

    def get_c_function(self):
        return colored('%(module)s.%(funcName)s' %
                       self.record.__dict__, 'yellow')

    def get_indented_message(self):
        from textwrap import TextWrapper
        lines = self.record.getMessage().splitlines()
        new_lines = []
        w = TextWrapper(width=66)  # 70 - 4
        for line in lines:
            for _line in w.wrap(line):
                new_lines.append(_line)
        return "\n".join(['    %s' % l for l in new_lines])


class ConsoleColorFormatter(logging.Formatter):
    """
    A nice color formatter for the logging module, providing some extra
    context arguments for the log output:

    c_date
        The colored full date (``%(asctime)s,%(msecs)03d``)

    c_asctime
        The colored ``asctime``

    c_leveltag
        The colored level "tag"

    c_levelname
        The colored level name

    c_name
        The colored logger name (``[%(name)s]``)

    c_function
        The colored module/function name (``%(module)s.%(funcName)s``)

    indented_message
        The message, wrapped to fit 70 columns and indented by four spaces.
    """

    def __init__(self, fmt=None, datefmt=None):
        if fmt is None:
            fmt = LOG_FORMAT_CONSOLE_COLOR
        if datefmt is None:
            datefmt = LOG_DATEFMT_CONSOLE_COLOR
        logging.Formatter.__init__(self, fmt=fmt, datefmt=datefmt)

    def format(self, record):
        record.message = record.getMessage()

        #if string.find(self._fmt, "%(asctime)") >= 0:

        record.asctime = self.formatTime(record, self.datefmt)

        formatted_record = self._fmt % LazyRecordColorer(record)

        if record.exc_info:
            # Cache the traceback text to avoid converting it multiple times
            # (it's constant anyway)
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)

        if record.exc_text:
            if formatted_record[-1:] != "\n":
                formatted_record += "\n"
            formatted_record += record.exc_text

        return formatted_record
