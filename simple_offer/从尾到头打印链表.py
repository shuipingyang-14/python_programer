# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 11:59
# @python  : python 3.7
# @Author  : 水萍
# @File    : 从尾到头打印链表.py
# @Software: PyCharm


def reversePrint(head):
	res = []
	while head:
		res.append(head.val)
		head = head.next
	return res[::-1]