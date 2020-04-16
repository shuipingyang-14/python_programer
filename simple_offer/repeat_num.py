# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 15:08
# @python  : python 3.7
# @Author  : 水萍
# @File    : repeat_num.py
# @Software: PyCharm


def find_repeat_num_1(nums):
	"""
	先给数组排序后查找
	时间复杂度：O(NlogN)
    空间复杂度：O(N)
	:param nums: 数组
	:return: 重复数字
	"""
	nums.sort()
	temp = -1
	for num in nums:
		if num == temp:
			return num
		else:
			temp = num


def find_repeat_num_2(nums):
	"""
	哈希表查找
	时间复杂度：O(N)
	空间复杂度：O(N)
	:param nums: 数组
	:return: 重复数字
	"""
	my_set = set()
	for num in nums:
		if num in my_set:
			return num
		else:
			my_set.add(num)


def find_repeat_num_3(nums):
	"""
	数组性质
	时间复杂度：O(N)
	空间复杂度：O(1)
	:param nums: 数组
	:return: 重复数字
	"""
	for i in range(len(nums)):
		while nums[i] != i:
			if nums[nums[i]] == nums[i]:
				return nums[i]
			else:
				temp = nums[i]
				nums[i] = nums[temp]
				nums[temp] = temp

if __name__ == "__main__":
	nums = [1,2,3,4,5,4,6,6,7,8]
	num1 = find_repeat_num_1(nums)
	num2 = find_repeat_num_2(nums)
	num3 = find_repeat_num_3(nums)
	print(num1, num2, num3)