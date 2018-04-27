from tempfile import TemporaryDirectory
from unittest import TestCase,main

from util import to_str

class UtilTest(TestCase):
	def test_to_str_bytes(self):
		self.assertEqual('hello',to_str(b'hello'))

	def test_to_str_str	(self):
		self.assertEqual('hello',to_str('hello'))

	# def test_to_str_bad(self):
	# 	self.assertEqual(TypeError,to_str,object())

class MyTest(TestCase):
	def setUp(self):
		self.test_dir = TemporaryDirectory()
	def tearDown(self):
		self.test_dir.cleanUp()

if __name__ == '__main__':
    main()


