# encoding=utf-8

class LazyDB(object):
	def __init__(self):
		self.exists = 5

	def __getattr__(self, name):
		value = 'Value for %s' %name
		setattr(self,name,value)
		return value

data = LazyDB()

print('Before',data.__dict__)
print('foo',data.foo)
print('After',data.__dict__)

class LogginglazyDB(LazyDB):
	def __getattr__(self, name):
		print('Called __getattr__(%s)' %name)
		return super().__getattr__(name)

data = LogginglazyDB()

print('exists:',data.exists)
print('foo:',data.foo)
print('foo:',data.foo)

class ValidatingDB(object):
	def __init__(self):
		self.exists = 5

	def __getattribute__(self, name):
		print('Called__getattribute__(%s)'% name)
		try:
			return super().__getattribute__(name)
		except AttributeError:
			value = 'Value for %s' %name
			setattr(self,name,value)
			return value

data = ValidatingDB()
print('exists:',data.exists)
print('foo:',data.foo)
print('foo:',data.foo)

class MissingPropertyDB(object):
	def __getattr__(self, item):
		if item == "bad_name":
			raise AttributeError('%s is missing' %item)

#
# data = MissingPropertyDB()
# data.bad_name

class SavingDB(object):
	def __setattr__(self, key, value):
		super().__setattr__(key,value)


class LoggingSavingDB(object):
	def __setattr__(self, key, value):
		print('called __setattr__(%s,%r)' %(key,value))
		super().__setattr__(key,value)

data = LoggingSavingDB()

print('before',data.__dict__)
data.foo = 5
print('after',data.__dict__)
data.foo = 7
print('Finally',data.__dict__)

class BrokenDictionaryDB(object):
	def __init__(self,data):
		self._data = data

	def __getattribute__(self, item):
		print('called __getattibute__(%s)' %item)
		return self._data[item]