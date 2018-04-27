# encoding=utf-8

names = ['Socreates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x))

print(names)


def increment_with_report(current, increment):
	added_count = 0

	def missing():
		nonlocal added_count  # Stateful closure
		added_count += 1
		return 0

# 	result = defaultdict(missing, current)
# 	for key, amout in increment:
# 		result[key] += amout
# 	return result, added_count
#
#
# class CountMissing(object):
# 	def __init__(self):
# 		self.added = 0
#
# 	def missing(self):
# 		self.added += 1
# 		return 0

#
# counter = CountMissing()
# result = defaultdict(counter.missing,current)
#
# for key ,amount in increments:
# 	result[key]+=amount
#
# assert counter.added==2

class BetterCountMissing(object):
	def __init__(self):
		self.added = 0
	def __call__(self, *args, **kwargs):
		self.added+=1
		return 0

counter2 = BetterCountMissing()
counter2()
assert callable(counter2)

# result  = defaultdict(counter2,current)

