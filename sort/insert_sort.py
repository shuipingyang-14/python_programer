# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 18:39
# @python  : python 3.7
# @Author  : 水萍
# @File    : insert_sort.py
# @Software: PyCharm


def insert_sort(lists):
	"""
	插入排序
	:param lists: 待排序数组
	:return: 排序完成数组
	"""
	count = 0
	for i in range(1, len(lists)):
		keys = lists[i]
		j = i-1
		while j >= 0:
			if lists[j] > keys:
				lists[j+1] = lists[j]
				lists[j] = keys
			j -= 1
			count += 1
	print(count)
	return lists


if __name__ == "__main__":
	list1 = [38, 65, 97, 76, 13, 27, 49]
	list2 = insert_sort(list1)
	print(list2)
