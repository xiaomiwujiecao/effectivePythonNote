#encoding-utf-8

# 单次切片操作 不要同时制定start end stride

# 奇偶数分组

a = ['red','orange','yellow','green','blue','purple']

odds = a[::2]

evens = a[1::2]
print(odds)
print(evens)

# 字符串反转

x = b"mongoose"
y = x[::-1]
print(y)

# UTF-8 不奏效
try:
	w = "谢谢"
	x = w.encode('utf-8')
	y = x[::-1]
	z = y.decode('utf-8')
except UnicodeDecodeError:
	print('字符转码错误！')

# 其他的负进值

ohthers = ['a','b','c','d','e','f','g','h']

other_odds =  ohthers[::2]
print(other_odds)
other_odds_reverse = ohthers[::-2]
print(other_odds_reverse)

print(ohthers[2::2])
print(ohthers[-2::-2])
print(ohthers[-2:2:-2])
print(ohthers[2:2:-2])

# 步进式切片 推荐方式

step_1 = ohthers[::2]
print(step_1)
step_2 = step_1[1:-1]
print(step_2)
