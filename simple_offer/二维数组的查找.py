# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 22:29
# @python  : python 3.7
# @Author  : 水萍
# @File    : 二维数组的查找.py
# @Software: PyCharm


def find_num_1(matrix, target):
	"""
	二维数组的查找
	:param matrix: 数组
	:param target: 要查找的数
	:return: 
	"""
	for index in matrix:
		if target in index:
			return True
	return False


def find_num_2(matrix, target):
	"""
	从上到下遍历数组
	:param matrix:
	:param target:
	:return:
	"""
	if matrix == []:
		return False
	right = len(matrix[0])
	top = len(matrix)
	i = top - 1
	j = 0
	while i >= 0 and j < right:
		if matrix[i][j] == target:
			return True
		elif matrix[i][j] < target:
			j += 1
		else:
			i -= 1
	return False


if __name__ == "__main__":
	# matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
	# matrix = []
	matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
	# matrix = [[15]]
	target = 20
	# print(find_num_1(matrix, target))
	print(find_num_2(matrix, target))