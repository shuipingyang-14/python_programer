# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 14:13
# @python  : python 3.7
# @Author  : 水萍
# @File    : 删除链表的节点.py
# @Software: PyCharm


def deleteNode(head, val):
	if head.val == val:
		return head.next
	pre = head
	cur = head.next
	while cur and cur.val != val:
		pre = cur
		cur = cur.next
	if cur:
		pre.next = cur.next
	return head
