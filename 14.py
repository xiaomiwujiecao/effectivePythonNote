# encoding=utf-8

def divide(a, b):
	try:
		return a / b
	except ZeroDivisionError:
		return None


# result = divide(1, 0)
# if result is None:
# 	print('Invalid inputs')

# x, y = 0, 5


# result = divide(x, y)
# print(result)
# if not result:
# 	print('非法输入')


def divide2(a, b):
	try:
		return True, a / b
	except ZeroDivisionError:
		return False, None


# success, result = divide2(x, y)
# if not success:
# 	print('invalid inputs')


# Wrong wording

# _,result = divide2(x,y)
# if not result:
# 	print('invalid inputs')

def divide3(a, b):
	try:
		return a / b
	except ZeroDivisionError as e:
		raise ValueError('Invalid inputs') from e


x, y = 5, 2
try:
	result = divide3(x, y)
except ValueError:
	print('Invalid inputs')
else:
	print('Result is %.1f' %result)

