def normalize(numbers):
	total = sum(numbers)
	result = []
	for value in numbers:
		percent = 100 * value / total
		result.append(percent)
	return result


# visits = [15, 35, 80]
# percentages = normalize(visits)
#
# print(percentages)

def read_visits(data_path):
	with open(data_path) as f:
		for line in f:
			yield int(line)


it = read_visits('/tmp/my_numbers.txt')
percentage2 = normalize(it)
print(percentage2)


def normalize_copy(numbers):
	numbers = list(numbers)
	total = sum(numbers)
	result = []
	for value in numbers:
		percent = 100 * value / total
		result.append(percent)
	return result


it = read_visits("/tmp/my_numbers.txt")
percentage2 = normalize_copy(it)
print(percentage2)


# def normalize_func(get_iter):
# 	total = sum(get_iter())
# 	result = []
# 	for value in get_iter():
# 		percent = 100*value/total
# 		result.append(percent)
# 	return result
#
path = '/tmp/my_numbers.txt'
# percentage3 = normalize_func(lambda: read_visits(path))
#
# print(percentage3)

class ReadVisits(object):
	def __init__(self, data_path):
		self.data_path = data_path

	def __iter__(self):
		with open(self.data_path) as f:
			for line in f:
				yield int(line)

visits = ReadVisits(path)
percentage4 = normalize(visits)
print(percentage4)

def normalize_defensive(numbers):
	if iter(numbers) is iter(numbers):
		raise TypeError('Must apply a container')
	total = sum(numbers)
	result = []
	for value in numbers:
		percent = 100*value/total
		result.append(percent)
	return result

