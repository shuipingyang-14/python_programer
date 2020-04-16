# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 18:32
# @python  : python 3.7
# @Author  : 水萍
# @File    : select_sort.py
# @Software: PyCharm


def select_sort(lists):
	"""
	选择排序
	:param lists: 待排序树组
	:return: 排序完成数组
	"""
	count = 0
	for i_index in range(0, len(lists)):
		min = i_index
		for j_index in range(i_index+1, len(lists)):
			# 找出最小值
			if lists[min] > lists[j_index]:
				min = j_index
			count += 1
		lists[min], lists[i_index] = lists[i_index], lists[min]
	print(count)
	return lists


if __name__ == "__main__":
	list1 = [38, 65, 97, 76, 13, 27, 49]
	list2 = select_sort(list1)
	print(list2)
