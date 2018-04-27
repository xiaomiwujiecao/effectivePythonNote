# encoding=utf-8

for i in range(3):
	print('Loop %d' % i)
else:
	print('else block!')

for i in range(3):
	print('Loop %d' % i)
	if i == 1:
		break
else:
	print('else block')

for x in []:
	print('never runs')
else:
	print('else block')

while False:
	print('Never runs')
else:
	print('While Else block')

a = 4
b = 9
for i in range(2, min(a, b) + 1):
	print('Testing', i)
	if a % i == 0 and b % i == 0:
		print('not coprime')
		break
else:
	print('Coprime')


def coprime(a, b):
	for i in range(2, min(a, b) + 1):
		if a % i == 0 and b % i == 0:
			return False
	return True

def coprime2(a,b):
	is_coprime = True
	for i in range(2,min(a,b)+1):
		if a%i==0 and b%i ==0:
			break
			return False
	return is_coprime	