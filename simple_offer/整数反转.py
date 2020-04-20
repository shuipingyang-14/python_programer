# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 18:59
# @python  : python 3.7
# @Author  : 水萍
# @File    : 整数反转.py
# @Software: PyCharm


def reverse_num_1(x):
	"""
	反转数字
	:param x: 传入的数字
	:return: 反转后数字
	"""
	if -10 < x < 10:
		return x
	str_x = str(x)
	if str_x[0] != "-":
		str_x = str_x[::-1]
		x = int(str_x)
	else:
		str_x = str_x[:0:-1]
		x = int(str_x)
		x = -x
	if -2147483648 < x < 2147483647:
		return x
	else:
		return 0


def reverse_num_2(x):
	"""
	反转数字
	:param x: 传入的数字
	:return: 反转后数字
	"""
	s = []
	x = list(str(x))
	x.reverse()
	s.append(x)
	str1 = ''
	if s[0][len(s[0])-1] == '-':
		str1 = '-'
	str2 = ''.join(s[0])
	str1 += str2
	if str1[len(str1)-1] == '-':
		if  -2147483648 < int(str1[:-1]) <  2147483648:
			return int(str1[:-1])
		else:
			return 0
	else:
		if  -2147483648 < int(str1) <  2147483648:
			return int(str1)
		else:
			return 0


if __name__ == "__main__":
	x = 123
	# x = -123
	# res = reverse_num_1(x)
	res = reverse_num_2(x)
	print(res)