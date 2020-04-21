# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 16:41
# @python  : python 3.7
# @Author  : 水萍
# @File    : 链表倒数第k个节点.py
# @Software: PyCharm


def getKthFromEnd(head, k):
	count = 0
	cur = head
	while head:
		count += 1
		head = head.next
	tmp = count - k
	i = 0
	while i<tmp:
		cur = cur.next
		i += 1
	return cur