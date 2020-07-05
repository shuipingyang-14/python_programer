# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 22:17
# @python  : python 3.7
# @Author  : 水萍
# @File    : 2 list_operation.py
# @Software: PyCharm


l1 = [100, "hello", True, [1, 2, 3]]
# 1.切片
print(l1[:2])
l2 = [1, 2, 3, 'a', 'b', 'c']
print(l2[1:-2:2])

# 2.列表创建
l1 = [1, 2, 3]
l1 = list("11111")
print(l1)

# 3.增加元素
l1 = []
l1.append('a')
l1.append('b')
l1.append('c')
l1.insert(2, 'd')
l1.extend('1234')
l1.extend(['123', ''])
print(l1)
l1.pop()
print(l1)

# 4.删除元素
l1 = ['a', 'b', 'd', 'c', '1', '2', '3', '4', '123']
l1.pop()  # 默认删除最后一个元素
print(l1)
l1.pop(-2)  # 按照索引删除，返回删除元素
print(l1)
l1.remove('a')  # 删除指定元素，如果有重名元素，默认删除左边第一个
print(l1)
del l1[-2]  # 按照索引删除
print(l1)
del l1[::2]  # 按照切片删除
print(l1)
print(l1)
l1.clear()  # 清空列表
print(l1)

# 5.更改元素
l1 = [1, 2, 3]
l1[1] = 'a'
print(l1)
l1[2:] = "sdfg"
print(l1)
l1[::2] = "abc"
print(l1)

# 6.查找元素
l1 = [1, 2, 3, 4, 5]
for i in l1:
	print(i)

# 7.嵌套
l1 = [1, 2, "hello", ['a', 'b', 'c']]
l1[2] = l1[2].upper()
print(l1)
l1[-1].append('d')
print(l1)
for index in range(0,len(l1[3])):
	if l1[3][index] == 'b':
		l1[3][index] = 'bbb'
print(l1)

# 8.count
l = [1,2,3,2,3,4]
print(l.count(3))  # 统计元素个数

# 9.index
l = [1,2,3,2,3,4]
print(l.index(3))  # 通过元素找索引，找到第一个就返回

# 10.sort
l = [1,2,3,2,3,4]
l.sort()
print(l)  # 从小到大排序
l.sort(reverse=False)
print(l)  # 从大到小排序

# 11.reverse
l = [1,2,3,2,3,4]
l.reverse()   # 反转列表
print(l)

# 12.列表想加
l1 = [1,2,3,4]
l2 = [4,5,6,7]
print(l1+l2)

# 列表与数字相乘
l1 = [1,2,3]
print(l1*3)

l1 = [11,22,33,44,55]
# 删除索引为奇数的值
del l1[1::2]
print(l1)
l1 = [11,22,33,44,55]
for index in range(len(l1)-1, -1, -1):
	if index %2 != 0:
		l1.pop(index)
print(l1)