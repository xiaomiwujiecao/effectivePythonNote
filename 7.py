# encoding=utf-8

# 用列表推导来取代map和filter

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x ** 2 for x in a]
print(squares)
squares_lambda = map(lambda x: x ** 2, a)
print(squares_lambda)

# 计算可以被2整除的数

even_squares = [x ** 2 for x in a if x % 2 == 0]

print(even_squares)

even_squares_lambda = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0,a))
try:
	assert even_squares == list(even_squares_lambda)
except AssertionError:
	print('断言失败')
# 字典与集 也有和列表类似的推导机制

chile_ranks = {'ghost':1,'habnero':2,'cayenne':3}
rank_dict = {value:key for key,value in chile_ranks.items()}

print(rank_dict)

chile_len_set = {len(name) for name in rank_dict.values()}

print(chile_len_set)