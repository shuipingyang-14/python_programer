# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 10:20
# @python  : python 3.7
# @Author  : 水萍
# @File    : 旋转数组的最小数字.py
# @Software: PyCharm


def minArray(numbers):
	for i in range(0, len(numbers) - 1):
		if numbers[i + 1] < numbers[i]:
			return numbers[i + 1]
	return numbers[0]


def minArray_1(numbers):
	i = 0
	j = len(numbers)-1
	while i < j:
		m = (i+j) // 2
		if numbers[m] > numbers[j]:
			i = m +1
		elif numbers[m] < numbers[j]:
			j = m
		else:
			j -= 1
	return numbers[i]


if __name__ == "__main__":
	nums = [1,2,3,4,5]
	nums1 = [2,3,4,5,1]
	res = minArray(nums)
	res1= minArray_1(nums)
	print(res, res1)