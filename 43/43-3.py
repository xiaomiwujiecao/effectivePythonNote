# encoding=utf-8
import logging

from decorator import contextmanager

with open('/tmp/my_output_.txt','w') as handle:
	handle.write('this is some data!')

@contextmanager
def log_level(level,name):
	logger = logging.getLogger(name)
	old_level = logger.getEffectiveLevel()
	logger.setLevel(level)
	try:
		yield logger
	finally:
		logger.setLevel(old_level)

with log_level(logging.DEBUG,'my-log') as logger:
	logger.debug('this is my message!')
	logging.debug('this will not print')

