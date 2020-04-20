# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 14:04
# @python  : python 3.7
# @Author  : 水萍
# @File    : 打印从1到最大的n位数.py
# @Software: PyCharm


def printNumbers(n):
	res = []
	num = pow(10, n)
	for i in range(1, num):
		res.append(i)
	return res


if __name__ == "__main__":
	num = 3
	res = printNumbers(num)
	print(res)