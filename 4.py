from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=',keep_blank_values=True)

print(my_values )

print('Red   ',my_values.get('red'))
print('Green   ',my_values.get('green'))
print('Opcity   ',my_values.get('opcityÎ'))

# 三元运算符

red = my_values.get('red',[''])
red = int(red[0]) if red[0] else 0
print(red)

# 辅助函数

def get_firsr_int (values,key,default=0):
	found = values.get(key,[''])
	if found[0]:
		found = int(found[0])
	else:
		found = default
	return found

green = get_firsr_int(my_values,'green')

print(green)