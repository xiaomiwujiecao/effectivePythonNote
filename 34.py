# encoding=utf-8
import json


# class Serializable(object):
# 	def __init__(self,*args):
# 		self.args = args
#
# 	def serialize	(self):
# 		return json.dumps({'args':self.args})
#
# class Point2D(Serializable):
# 	def __init__(self,x,y):
# 		super().__init__(x,y)
# 		self.x =x
# 		self.y = y
#
# 	def __repr__(self):
# 		return 'point2d(%d,%d)' % (self.x,self.y)
#
# point = Point2D(5,3)
#
# print('Object:',point)
#
# print('Serialized',point.serialize())
#
# class Deserializable(Serializable):
# 	@classmethod
# 	def deserialize(cls,json_data):
# 		params = json.loads(json_data)
# 		return cls(*params['args'])
#
#
# # class BetterPoint2D(Deserializable):
# # 	def __init__(self,*args):
# # 		self.args = args
#
# class BetterSerializable(object):
# 	def __init__(self,*args):
# 		self.args = args
#
# 	def serialize(self):
# 		return json.dumps({
# 			'class':self.__class__.__name__,
# 			'args':self.args
# 		})
#
# 	def __repr__(self):
# 		pass
#
#
registry = {}

def register_class(target_class):
	registry[target_class.__name__] = target_class
#
# def deserialize(data):
# 	params = json.loads(data)
# 	name = params['class']
# 	target_class = registry[name]
# 	return target_class(*params['args'])
#
#
# class EventBetterPoint2D(BetterSerializable):
# 	def __init__(self,x,y):
# 		super().__init__(x,y)
# 		self.x = x
# 		self.y = y
#
# register_class(EventBetterPoint2D)
#
# point = EventBetterPoint2D(5,3)
# print('Before',point)
# data = point.serialize()
# print('Serialized',data)
# after = deserialize(data)
# print('After',after)
#
#
# class Point3D(BetterSerializable):
# 	def __init__(self,x,y,z):
# 		super().__init__(x,y,z)
# 		self.x = x
# 		self.y = y
# 		self.z = z
#
#

class Meta(type):
	def __new__(meta,name,bases,class_dict):
		cls = type.__new__(meta,name,bases,class_dict)
		register_class(cls)
		return cls

class RegisterdSerializable(BetterSerializable,metaclass=Meta):
	pass