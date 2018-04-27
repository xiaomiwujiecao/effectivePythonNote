# encoding=utf-8

print('foo bar')

a = '\x07'

print(repr(a))

b = eval(repr(a))

assert a == b


print(repr(5))
print(repr('5'))

class OpaqueClass(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __repr__(self):
		return 'BetterClass (%d,%d)' %(self.x,self.y)


object = OpaqueClass(1,2)

print(object.__dict__)
print(object)
