# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 18:59
# @python  : python 3.7
# @Author  : 水萍
# @File    : merge_sort.py
# @Software: PyCharm

count = 0


def merge(left, right):
	i = j = 0
	global count
	result = []
	while i<len(left) and j<len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
		count += 1
	result += left[i:]
	result += right[j:]
	print(count)
	return result


def merge_sort(lists):
	"""
	归并排序
	:param lists: 待排序树组
	:return: 排序完成数组
	"""
	if len(lists) <= 1:
		return lists
	num = len(lists)/2
	list1 = []
	list2 = []
	for index in range(len(lists)):
		if index < num:
			list1.append(lists[index])
		else:
			list2.append(lists[index])
	left = merge_sort(list1)
	right = merge_sort(list2)
	return merge(left, right)


if __name__ == "__main__":
	list1 = [38, 65, 97, 76, 13, 27, 49]
	list2 = merge_sort(list1)
	print(list2)