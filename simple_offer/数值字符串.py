# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 14:20
# @python  : python 3.7
# @Author  : 水萍
# @File    : 数值字符串.py
# @Software: PyCharm


def isNumber(s):
	try:
		float(s)
		return True
	except:
		return False


if __name__ == '__main__':
	str = "12e+5.4"
	res = isNumber(str)
	print(res)