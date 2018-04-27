# encoding=utf-8

# 不要使用含有两个以上表达式的列表推导

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = [x for row in matrix for x in row]

print(flat)

squared = [[x ** 2 for x in row] for row in matrix]

print(squared)

# 从数字列表中 选择大于4的偶数

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = [x for x in a if x > 4 if x % 2 == 0]

c = [x for x in a if x > 4 and  x % 2 == 0]

print(b)

print(c)

# 编写 从矩阵中挑出能被3整除 各行纸盒大于等于10的单元格

matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

filtered = [[x for x in row if x%3==0] for row in matrix2 if sum(row)>=10]

print(filtered)