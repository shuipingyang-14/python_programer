# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 18:55
# @python  : python 3.7
# @Author  : 水萍
# @File    : bubble_sort.py
# @Software: PyCharm


def bubble_sort(lists):
	"""
	冒泡排序
	:param lists: 待排序数组
	:return: 排序完成的数组
	"""
	count = 0
	for i in range(len(lists)-1):
		for j in range(len(lists)-i-1):
			if lists[j] > lists[j+1]:
				lists[j],lists[j+1] = lists[j+1], lists[j]
			count += 1
	print(count)
	return lists


if __name__ == "__main__":
	list1 = [38, 65, 97, 76, 13, 27, 49]
	list2 = bubble_sort(list1)
	print(list2)