# encoding-utf-8

# Extend collections.abc to implement custom container type

# class FrequencyList(list):
# 	def __init__(self, members):
# 		super().__init__(members)
#
# 	def frequency(self):
# 		counts = {}
# 		for item in self:
# 			counts.setdefault(item, 0)
# 			counts[item] += 1
# 		return counts
#
#
# foo = FrequencyList(['a', 'b', 'a', 'c', 'b', 'a', 'd'])
#
# print('Length is ', len(foo))
#
# foo.pop()
# print('after pop', repr(foo))
# print('frenquency', foo.frequency())
#
#
# class BinaryNode(object):
# 	def __init__(self, value, left=None, right=None):
# 		self.value = value
# 		self.left = left
# 		self.right = right
#
#
# bar = [1, 2, 3]
# bar[0]
# bar.__getitem__(0)
#
#
# class IndexableNode(BinaryNode):
# 	def _search(self, count, index):
# 		pass
#
# 	def __getitem__(self, index):
# 		found, _ = self._search(0, index)
# 		if not found:
# 			raise IndexError('Index out of range')
# 		return found.value
#
# 	def __len__(self):
# 		_,count = self._search(0,None)
# 		return count
#
# tree = IndexableNode(
# 	10,
# 	left=IndexableNode(
# 		5,
# 		left=IndexableNode(2),
# 		right=IndexableNode(
# 			6, right=IndexableNode(7)
# 		)
# 	),
# 	right=IndexableNode(
# 		15, left=IndexableNode(11)
# 	)
# )

from collections.abc import Sequence

class BadType(Sequence):
	pass

foo = BadType()

# TypeError: Can't instantiate abstract class BadType with abstract methods __getitem__, __len__

