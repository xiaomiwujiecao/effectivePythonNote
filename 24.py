# encoding=utf-8
import os
from threading import Thread
from tempfile import TemporaryDirectory

class InputData(object):
	def read(self):
		raise NotImplementedError


class PathINputData(InputData):
	def __init__(self, path):
		super().__init__()
		self.path = path

	def read(self):
		return open(self.path).read()


class Worker(object):
	def __init__(self, input_data):
		self.input_data = input_data
		self.result = None

	def map(self):
		raise NotImplementedError

	def reduce(self, other):
		raise NotImplementedError


class LineCountWorker(object):
	def map(self):
		data = self.input_data.read()
		self.result = data.count('\n')

	def reduce(self, other):
		self.result += other.result


def generate_inputs(data_dir):
	for name in os.listdir():
		yield PathINputData(os.path.join(data_dir,name))

def create_worker(inputs_list):
	workers = []
	for input_data in inputs_list:
		workers.append(LineCountWorker(input_data))

	return workers

def execute(workers):
	threads = [Thread(target = w.map) for w in workers]
	for thread in threads:thread.start()
	for thread in threads:thread.join()

	first,rest = workers[0],workers[1:]
	for worker in rest:
		first.reduce(worker)

def mapreduce(data_dir):
	inputs = generate_inputs(data_dir)
	workers  = create_worker(inputs)
	return  execute(workers)

def write_test_files(tmpdir):
	#sad
	print(tmpdir)

with TemporaryDirectory() as tmpdir:
	write_test_files(tmpdir)
	result = mapreduce(tmpdir)


class GenericInputData(object):
	def read(self):
		raise NotImplementedError

	@classmethod
	def generate_inputs(cls,config):
		data_dir = config['data_dir']
		for name in os.listdir(data_dir):
			yield cls(os.path.join(data_dir,name))

class GenericWorker(object):
	# ...
	def map(self):
		raise NotImplementedError
	def reduce(self,other):
		raise NotImplementedError

	@classmethod
	def create_worer(cls,input_class,config):
		wokers = []
		for input_data in input_class.generate_inputs(config):
			wokers.append(cls(input_class))