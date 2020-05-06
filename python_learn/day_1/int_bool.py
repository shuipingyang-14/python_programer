# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 22:27
# @python  : python 3.7
# @Author  : 水萍
# @File    : int_bool.py
# @Software: PyCharm

# bit_length:有效二进制的长度
i = 4
print(i.bit_length())  # 3
i = 8
print(i.bit_length())  # 4
i = 16
print(i.bit_length())  # 5
i = 42
print(i.bit_length())  # 6

# bool
"""
True  1   
False  0
非零是True,0是False
"""

# str->int
i1 = 10
print(type(i1))   # int
s2 = str(i1)
print(type(s2))   # str
s = "100"
print(type(s))   # str
s1 = int(s)
print(type(s1))   # int

# str->bool
"""
非空即True
"""
s1 = ''
print(bool(s1))   # False
s1 = ' '
print(bool(s2))   # True

s = input("输入内容：")
if s:
	print("有内容")
else:
	print("没有输入内容")