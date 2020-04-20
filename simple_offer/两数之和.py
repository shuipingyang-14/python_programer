# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 10:59
# @python  : python 3.7
# @Author  : 水萍
# @File    : 两数之和.py
# @Software: PyCharm


def twoSum(nums, target):
	"""
	找到 num2 = target - num1，是否也在 list 中
	:param nums: 查找的数组
	:param target: 查找的目标数字
	:return: 查找到的数组
	"""
	lens = len(nums)
	j = -1
	for i in range(lens):
		if (target - nums[i]) in nums:
			if (nums.count(target - nums[i]) == 1) & (
					target - nums[i] == nums[i]):  # 如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
				continue
			else:
				j = nums.index(target - nums[i], i + 1)  # index(x,i+1)是从num1后的序列后找num2
				break
	if j > 0:
		return [i, j]
	else:
		return []


def twoSum_1(nums, target):
	"""
	找到 num2 = target - num1，是否也在 list 中
	:param nums: 查找的数组
	:param target: 查找的目标数字
	:return: 查找到的数组
	"""
	lens = len(nums)
	j = -1
	for i in range(1, lens):
		temp = nums[:i]
		if (target - nums[i]) in temp:
			j = temp.index(target - nums[i])
			break

	if j >= 0:
		return [j, i]


def twoSum_2(nums, target):
	"""
	找到 num2 = target - num1，是否也在 list 中
	:param nums: 查找的数组
	:param target: 查找的目标数字
	:return:
	"""
	hashmap = {}
	for ind, num in enumerate(nums):
		hashmap[num] = ind
	for i, num in enumerate(nums):
		j = hashmap.get(target - num)
		if j is not None and i != j:
			return [i, j]


def twoSum_3(nums, target):
	"""
	找到 num2 = target - num1，是否也在 list 中
	:param nums: 查找的数组
	:param target: 查找的目标数字
	:return:
	"""
	d = {}
	for i, item in enumerate(nums):
		tmp = target - item
		for key, value in d.items():
			if value == tmp:
				return [key, i]
		d[i] = item
	return None


def twoSum_4(nums, target):
	"""
	找到 num2 = target - num1，是否也在 list 中
	:param nums: 查找的数组
	:param target: 查找的目标数字
	:return:
	"""
	hashmap = {}
	for i, num in enumerate(nums):
		if hashmap.get(target - num) is not None:
			return [i, hashmap.get(target - num)]
		hashmap[num] = i
	# 解决list中有重复值或target-num=num的情况


def twoSum_5(numbers, target):
	"""
	找到 num2 = target - num1，是否也在 list 中
	:param nums: 查找的有序数组
	:param target: 查找的目标数字
	:return:
	"""
	left = 0
	right = len(numbers)-1
	while left <right:
		if numbers[left] + numbers[right] == target:
			return [left+1, right+1]
		elif numbers[left] + numbers[right] > target:
			right -= 1
		else:
			left += 1


if __name__ == "__main__":
	nums = [2, 4, 5, 7, 9, 11]
	target = 9
	res = twoSum(nums, target)
	res1 = twoSum_1(nums, target)
	res2 = twoSum_2(nums, target)
	res3 = twoSum_3(nums, target)
	res4 = twoSum_4(nums, target)
	res5 = twoSum_5(nums, target)
	print(res, res1, res2, res3, res4, res5)
