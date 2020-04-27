# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 16:18
# @python  : python 3.7
# @Author  : 水萍
# @File    : 调整奇数位于偶数前面.py
# @Software: PyCharm


def exchange(nums):
	i = 0
	j = len(nums)-1
	if len(nums) == 1:
		return nums
	if nums == []:
		return nums
	while i != j:
		if nums[i] % 2 != 0:
			i += 1
		else:
			if nums[j] %2 != 0:
				nums[i], nums[j] = nums[j], nums[i]
			else:
				j -= 1
	return nums


if __name__ == "__main__":
	nums = [1,2,3,4]
	res = exchange(nums)
	print(res)