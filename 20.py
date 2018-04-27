# encoding=utf-8
import datetime
import json
from time import sleep


# def log(message,when=datetime.datetime.now()):
# 	print('%s:%s'%(when,message))
#
# log('Hi There')
# sleep(0.1)
# log('Hi again')

def log(message, when=None):
	'''
	Log a message with a timestamp
	Args:
	message:Message to print.
	when:datetime of when the message occurred.
		Defaults to the present time.
	:param message:
	:param when:
	:return:
	'''
	when = datetime.datetime.now() if when is None else when
	print('%s:%s' % (when, message))


log('Hi There')
sleep(0.1)
log('Hi again')


# def decode(data,default={}):
# 	try:
# 		return  json.loads(data)
# 	except ValueError:
# 		return  default
def decode(data, default=None):
	'''

	:param data: JSON data to decode
	:param default: Value to return if decoding fails
	:return:
	'''
	if default is None:
		default = {}
	try:
		return json.loads(data)
	except ValueError:
		return default


foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)

# assert foo is bar
