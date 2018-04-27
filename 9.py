# encoding=utf-8

# 用生成器表达式来改写数据量较大的列表推导

value = [len(x) for x in open('/tmp/my_file.txt')]

# print(value)

it = (len(x) for x in open('/tmp/my_file.txt'))

print(it) # <generator object <genexpr> at 0x10d9d10f8>
roots = ((x ,x**0.5) for x in it)

print(next(it))
print(next(roots))
