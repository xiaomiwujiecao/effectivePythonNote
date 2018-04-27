#encoding=utf-8

class MyBaseClass(object):
	def __init__(self,value):
		self.value = value

class MyChildClass(MyBaseClass):
	def __init__(self):
		MyBaseClass.__init__(self,5)

class TimesTwo(object):
	def __init__(self):
		self.value*=2

class PlusFive(object):
	def __init__(self):
		self.value+=5

class OneWay(MyBaseClass,TimesTwo,PlusFive):
	def __init__(self,value):
		MyBaseClass.__init__(self,value)
		TimesTwo.__init__(self)
		PlusFive.__init__(self)

foo = OneWay(5)

print('first ordering is (5*2)+5=',foo.value)

class AnotherWay(MyBaseClass,PlusFive,TimesTwo):
	def __init__(self,value):
		MyBaseClass.__init__(self,value)
		TimesTwo.__init__(self)
		PlusFive.__init__(self)

bar = AnotherWay(5)

print('second ordering is still is ', bar.value)