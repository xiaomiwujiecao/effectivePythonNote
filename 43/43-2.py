# encoding=utf-8
import logging

from decorator import contextmanager


def my_function():
	logging.debug('some debug data')
	logging.error('error log here')
	logging.debug('some debug data')

my_function()

@contextmanager
def debug_logging(level):
	logger = logging.getLogger()
	old_level = logger.getEffectiveLevel()
	logger.setLevel(level)
	try:
		yield
	finally:
		logging.setLevel(old_level)

with debug_logging(logging.DEBUG):
	print('Inside')
	my_function()
print('After')
my_function()

