# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 0:24
# @python  : python 3.7
# @Author  : 水萍
# @File    : 4 for循环.py
# @Software: PyCharm


s1 = "hello world"
# 循环打印字符
index = 0
while index < len(s1):
	print(s1[index])
	index += 1

for index in s1:
	if index == 'w':
		break
	print(index)
else:
	print("aaa")
