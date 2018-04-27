# encoding=utf-8
names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]

print(letters)

#  原始的写法
longest_nam = None
max_letters = 0
for i in range(len(names)):
	count = letters[i]
	if count > max_letters:
		longest_nam = names[i]
		max_letters = count
print(longest_nam)
# 使用 enumerate 迭代函数
for i,name in enumerate(names):
	count = letters[i]
	if count > max_letters:
		longest_name = name
		max_letters = count

# 使用zip函数 将两个以上的迭代器凤凰城为生成器

for name,count in zip(names,letters):
	if count > max_letters:
		longest_name = name
		max_letters = count
		print(name)

