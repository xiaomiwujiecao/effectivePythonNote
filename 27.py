# encoding=utf-8

class MyObject(object):
	def __init__(self):
		self.public_fild = 5
		self.__private_fild = 10

	def get_private_fild(self):
		return self.private_fild

foo = MyObject()
assert foo.public_fild == 5
# foo.__private_fild

class MyOhterObject(object):
	def __init__(self):
		self.__private_field = 71

	@classmethod
	def get_private_fild_of_instance(cls,instance):
			return instance.__private_field

bar  = MyOhterObject()
assert MyOhterObject.get_private_fild_of_instance(bar) == 71

class MyParentObject(object):
	def __init__(self):
		self.__private_field = 71

class MyChildObject(MyParentObject):
	def get_private_field(self):
		return self.__private_field

baz = MyChildObject()
# baz.get_private_field()

assert baz._MyParentObject__private_field == 71

print(baz.__dict__)



class MyBaseClass(object):
	def __init__(self,value):
		self.__value = value

class MyClass(MyBaseClass):
	def __init__(self,value):
		# This stores the user-supplied value for the object.
		# It should be coercible to a string . Once assigned for
		# the object it should be treated as immutable.

		self.__value = value

	def get_value(self):
		return str(self.__value)

foo = MyClass(5)
assert foo.get_value() == '5'

class MyIntegerSubClass(MyClass):
	def get_value(self):
		return int(self._MyClass__value)

foo = MyIntegerSubClass(5)
foo.get_value()

class ApiClass(object):
	def __init__(self):
		self.__value = 5

	def get(self):
		return self.__value

class Child(ApiClass):
	def __init__(self):
		super().__init__()
		self._value = 'hello'

a = Child()

print(a.get(),'and',a._value,'should be different')