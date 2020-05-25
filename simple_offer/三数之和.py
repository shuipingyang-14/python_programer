# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/22 23:31
@ file:     三数之和.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

def threeSum(nums):
    if len(nums) < 3:
        return []
    l1 = []
    l2 = []
    nums.sort()
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1,len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    l2.append(nums[i])
                    l2.append(nums[j])
                    l2.append(nums[k])
                    # l2.sort()
                    if l2  not in l1:
                        l1.append(l2)
                    l2 = []
    return l1


if __name__ == '__main__':
    l = [2,5,5,8,-7,-9,5,-1,-4,2,8,4,-6,-2,-2,9,-2,13,1,0,9,9,4,-13,13,3,-14,11,-5,-13,3,4,7,-15,-11,7,13,1,13,-14,11,-1,5,-10,12,11,14,-13,1,-8,3,-4,-14,14,-10,-15,-6,-9,3,-4,-7,-8,-15,8,-8,12,-8,13,-2,-9,14,-6,5,-3,-9,-6,-7,-10,-3,9,-2,7,-10,-9,-2,-5,13,7,-6,2,-12,-6,1,10,9,0,7,-13,-2,-9,-7,-2,-8,5,10,-1,6,-12,4,10,12,9,2,10,8,-15,12,6,-1,-9,-7,2]
    res = threeSum(l)
    print(res)