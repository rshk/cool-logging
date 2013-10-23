import io
import logging

from cool_logging.formatters import ConsoleColorFormatter

import re

r_escapes = r'(\x1b\[[0-9]+m)*'
r_date = r'[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3}'

re_debug_message = re.compile(r_escapes.join((
    r'^', ' DBUG ', ' ', ' test_logger ',
    ' in ', 'test_consolecolorformatter',
    '\.', 'test_console_color_formatter',
    ' at ', r_date, '\n',
    ' DBUG ', r'\s+Example DEBUG message\n$')))
re_error_message = re.compile(r_escapes.join((
    r'^', ' ERR! ', ' ', ' test_logger ',
    ' in ', 'test_consolecolorformatter',
    '\.', 'test_console_color_formatter',
    ' at ', r_date, '\n',
    ' ERR! ', r'\s+Example ERROR message\n$')))

def test_console_color_formatter():
    logger = logging.getLogger("test_logger")

    output = io.StringIO()
    handler = logging.StreamHandler(output)
    handler.setFormatter(ConsoleColorFormatter())
    handler.setLevel(logging.DEBUG)

    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)


    logger.debug(u"Example DEBUG message")
    text = output.getvalue()
    assert re_debug_message.match(text)
    output.seek(0)
    output.truncate()

    logger.error("Example ERROR message")
    text = output.getvalue()
    assert re_error_message.match(text)
    output.seek(0)
    output.truncate()
