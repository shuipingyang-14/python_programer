# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 21:37
# @python  : python 3.7
# @Author  : 水萍
# @File    : quick_sort.py
# @Software: PyCharm


def quick_sort(lists, left, right):
	"""
	快速排序
	:param lists: 待排序数组
	:param left: 排序的左索引
	:param right: 排序的右索引
	:return: 排序好的数组
	"""
	if left >= right:
		return lists
	key = lists[left]
	low = left
	high = right
	while left < right:
		while left < right and lists[right] >= key:
			right -= 1
		lists[left] = lists[right]
		while left < right and lists[left] <= key:
			left += 1
		lists[right] = lists[left]
	lists[right] = key
	quick_sort(lists, low, left-1)
	quick_sort(lists, left+1, high)
	return lists


if __name__ == "__main__":
	list1 = [38, 65, 97, 76, 13, 27, 49]
	list2 = quick_sort(list1, 0, len(list1)-1)
	print(list2)
