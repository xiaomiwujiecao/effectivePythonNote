# encoding=utf-8
from weakref import WeakKeyDictionary


class Homework(object):
	def __init__(self):
		self._grade = 0

	@property
	def grade(self):
		return self._grade

	@grade.setter
	def grade(self,value):
		if not (0<=value<=100):
			raise ValueError('Grade must be between 0 and 100')
		self._grade = value

galileo = Homework()

galileo.grade = 95

print(galileo.grade)

# class Exam(object):
# 	def __init__(self):
# 		self._writing_grade = 0
# 		self._math_grade = 0
#
# 	@staticmethod
# 	def _check_grade(value):
# 		if not (0<=value<=100):
# 			raise ValueError('Grade must be between 0 and 100')

class Grade(object):
	def __init__(self):
		self._value = WeakKeyDictionary()

	def __get__(self, instance, owner):
		if instance is None:
			return self
		return self._value.get(instance,0)

	def __set__(self, instance, value):
		if not(0<=value<=100):
			raise ValueError('Grade must be between 0 and 100')
		self._value[instance] = value

class Exam(object):
	math_grade = Grade()
	writing_grade = Grade()
	science_grade = Grade()


exam = Exam()

exam.writing_grade = 40

