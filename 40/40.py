# encoding=utf-8

def my_coroutine():
	while True:
		received = yield
		print('Received:',received)

it = my_coroutine()
next(it)

it.send('First')
it.send('Second')

def minimize():
	current = yield
	while True:
		value = yield  current
		current = min(value,current)

it = minimize()

next(it)

print(it.send(10))
print(it.send(4))
print(it.send(22))
print(it.send(-1))
