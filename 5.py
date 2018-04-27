# encoding=utf-8

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print('first four', a[:4])
print('Last four', a[-4:])
print('middle two', a[3:-3])

# 切割列表时 下表越界也不成问题

first_twenty_item = a[:20]
last_twenty_item = a[-20:]

# 访问列表中的单个元素时，下标不能越界，否则会导致异常

# error = a[20] # IndexError: list index out of range

# 使用负变量作为start索引 会出现一个问题

# copy = a[-0:]
# print(copy)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# b = a[:4]
'''
print('Before   ',b)

b[1]=99
print('After   ', b)

print('no change ',a)
print('Before a', a)

a[2:7]  = [99,22,14]

print("After   ",a)
'''
b = a[:]
c = a[:]
try:
	assert b == a and b is not a
except AssertionError:
	print('断言出错')

d = a
print('before d', d)

a[:] = [101, 102, 103]
try:
	assert a is d
except AssertionError:
	print('a is not d')

print('After d', d)