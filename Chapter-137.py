"""
Chapter 137: Logging
Section 137.1: Introduction to Python Logging

Example Configuration via an INI File
from logging.config import fileConfig

fileConfig('logging_config.ini')
logger = logging.getLogger()
logger.debug('often makes a very good meal of %s', 'visiting tourists')


Example Configuration via a Dictionary

from logging.config import dictConfig

logging_config = dict(
    version = 1,
    formatters = {
                'f': {'format':
                '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
                },
    handlers = {
                'h': {'class': 'logging.StreamHandler',
                'formatter': 'f',
                'level': logging.DEBUG}
                },
    root = {
                'handlers': ['h'],
                'level': logging.DEBUG,
                },
    )
dictConfig(logging_config)
logger = logging.getLogger()
logger.debug('often makes a very good meal of %s', 'visiting tourists')


Section 137.2: Logging exceptions

If you want to log exceptions you can and should make use of the logging.exception(msg) method:


>> logging.basicConfig()
>> try:
... raise Exception('foo')
... except:
... logging.exception('bar')
...
ERROR:root:bar
Traceback (most recent call last):
File "<stdin>", line 2, in <module>
Exception: foo


Do not pass the exception as argument:
>> try:
...     raise Exception(u'föö')
... except Exception as e:
...     logging.exception(e)
...

Trying to log an exception that contains unicode chars, this way will fail miserably. It will hide the stacktrace of the
original exception by overriding it with a new one that is raised during formatting of your logging.exception(e)
call.


Logging exceptions with non ERROR log levels
If you want to log an exception with another log level than ERROR, you can use the exc_info argument of the
default loggers:
logging.debug('exception occurred', exc_info=1)
logging.info('exception occurred', exc_info=1)
logging.warning('exception occurred', exc_info=1)

Accessing the exception's message
Be aware that libraries out there might throw exceptions with messages as any of unicode or (utf-8 if you're lucky)
byte-strings. If you really need to access an exception's text, the only reliable way, that will always work, is to use
repr(e) or the %r string formatting:

>> try:
...     raise Exception(u'föö')
    except Exception as e:
...     logging.exception('received this exception: %r' % e)

"""
import logging
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logger.debug('this is a %s test', 'debug')
