# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 13:02
# @python  : python 3.7
# @Author  : 水萍
# @File    : 3 tuple_operation.py
# @Software: PyCharm


tu = (100, 'hello', True, [1, 2, 3])
print(tu[:3])
print(len(tu))

# 1.查看
for i in tu:
	print(i)

# 2.增加
tu[-1].append('4')
print(tu)

# 3.删除
del tu[-1][0]
print(tu)

# 4.拆包
a, b = (1, 2)
print(a, b)
c = (1, 2)
a, b = c
print(a, b)
a, b = [11, 22]
print(a, b)

# 5. count
t = (1,2,2,2,2)
print(t.count(2))  # 统计元素出现个数