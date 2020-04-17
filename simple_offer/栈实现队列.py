# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 13:06
# @python  : python 3.7
# @Author  : 水萍
# @File    : 栈实现队列.py
# @Software: PyCharm

"""
栈无法实现队列功能： 栈底元素（对应队首元素）无法直接删除，需要将上方所有元素出栈。
双栈可实现列表倒序： 设有含三个元素的栈 A = [1,2,3] 和空栈 B = []
若循环执行 A 元素出栈并添加入栈 B ，直到栈 A 为空，则 A=[] , B = [3,2,1] ，即 栈 B 元素实现栈 A 元素倒序
利用栈 B 删除队首元素： 倒序后，B 执行出栈则相当于删除了 A 的栈底元素，即对应队首元素
"""


class CQueue:
	def __init__(self):
		self.A, self.B = [], []

	def appendTail(self, value):
		"""
        加入队尾 appendTail()函数： 将数字 val 加入栈 A 即可
        :param value:
        :return:
        """
		self.A.append(value)

	def deleteHead(self):
		"""
        当栈 B 不为空： B中仍有已完成倒序的元素，因此直接返回 B 的栈顶元素
        否则，当 A 为空： 即两个栈都为空，无元素，因此返回 −1
        否则： 将栈 A 元素全部转移至栈 B 中，实现元素倒序，并返回栈 B 的栈顶元素
        :return:
        """
		if self.B:
			return self.B.pop()
		if not self.A:
			return -1
		while self.A:
			self.B.append(self.A.pop())
		return self.B.pop()
