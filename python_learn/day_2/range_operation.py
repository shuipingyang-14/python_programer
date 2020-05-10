# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 13:12
# @python  : python 3.7
# @Author  : 水萍
# @File    : range_operation.py
# @Software: PyCharm


for i in range(1, 101):
	print(i)

for i in range(2, 101, 2):
	print(i)

for i in range(100, 0, -1):
	print(i)

l1 = [1, 2, 3, "hello", [1, 2, 3]]
for i in range(len(l1)):
	print(i)
