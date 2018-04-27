# encoding=utf-8
from collections import deque
from random import randint

fifo = deque()

fifo.append(1)
x = fifo.popleft()

print(x)

a = {}

a['foo'] = 1
a['bar'] = 2

while True:
	z =randint(99,1013)
	b = {}
	for i in range(z):
		b[i] = i
	b['foo'] = 1
	b['bar'] = 2

	for i in range(z):
		del b[i]

	if str(b) !=str(a):
		break


print(a)
print(b)
print('Equal?' ,a==b)
