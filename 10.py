# encoding=utf-8
'''
random_bits = 0
for i  in range(64):
	if randint(0,1):
		random_bits |=1 << i
'''

flavor_list = ['vanlila', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
	print('%s is delicious' % flavor)

for i in range(len(flavor_list)):
	flavor = flavor_list[i]
	print('%d:%s' % (i + 1, flavor))

for i,flavor in enumerate(flavor_list):
	print('%d:%s'%(i+1,flavor))

# 指定enumerate函数开始计数的值

for i,flavor in enumerate(flavor_list,1):
	print('%d:%s'%(i,flavor))