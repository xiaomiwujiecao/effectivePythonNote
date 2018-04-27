# encoding=utf-8
import collections


class SimpleGradeBook(object):
	def __init__(self):
		self._grades = {}

	def add_student(self, name):
		self._grades[name] = {}

	def report_grade(self, name, subject, grade):
		by_subject = self._grades[name]
		grade_list = by_subject.setdefault(subject, [])
		grade_list.append(grade)

	def average_grade(self, name):
		by_subject = self._grades[name]
		total, count = 0, 0
		for grades in by_subject.values():
			total += sum(grades)
			count += len(grades)
		return total / count


book = SimpleGradeBook()
book.add_student('xiaomi')
book.report_grade('xiaomi', 'Math', 75)
book.report_grade('xiaomi', 'Math', 65)
book.report_grade('xiaomi', 'Gym', 90)
book.report_grade('xiaomi', 'Gym', 95)

print(book.average_grade('xiaomi'))

Grade = collections.namedtuple('Gtade', ('score', 'weight'))


class Subject(object):
	def __init__(self):
		self._grades = []

	def report_grade(self, score, weight):
		self._grades.append(Grade(score, weight))

	def average_grade(self):
		total, total_weight = 0, 0
		for grade in self._grades:
			total += grade.score * grade.weight
			total_weight += grade.weight
		return total / total_weight


class Student(object):
	def __init__(self):
		self._subjects = {}

	def subject(self, name):
		if name not in self._subjects:
			self._subjects[name] = Subject()
		return self._subjects[name]

	def average_grade(self):
		total, count = 0, 0
		for subject in self._subjects.values():
			total += subject.average_grade()
			count += 1
		return total / count

class GradeBook(object):
	def __init__(self):
		self._students = {}
	def student(self,name):
		if name not in self._students:
			self._students[name]=Student()
		return self._students[name]

book2 = GradeBook()
albert = book2.student('xiaomi')
math = albert.subject('Math')

