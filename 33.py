class Meta(type):
	def __new__(meta,name,bases,class_dict):
		print((meta,name,bases,class_dict))
		return type.__new__(meta,name,bases,class_dict)

class MyClass(object,metaclass=Meta):
	stuff = 123

	def foo(self):
		pass


class ValidatePolygon(type):
	def __new__(meta,name,bases,class_dict):
		if bases!=(object,):
			if class_dict['sides']<3:
				raise ValueError("polygons need 3+ side")
		return type.__new__(meta,name,bases,class_dict)

class Polygnon(object,metaclass=ValidatePolygon):
	sides = None

	@classmethod
	def interior_angles(cls):
		return (cls.sides-2)*180


class Triangle(Polygnon):
	sides = 3

print('Before class')

class Line(Polygnon):
	print('before sides')
	sides = 1
	print('after sides')