# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/29 9:54
@ file:     最大几个数.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

def max_num(nums):
    temp = []
    inf = 0
    for i in range(3):
        temp.append(max(nums))
        nums.pop(nums.index(max(nums)))
    return temp

if __name__ == '__main__':
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 24, 37, 2]
    res = max_num(nums)
    print(res)
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 23, 37, 2]
    res = max_num(nums)
    print(res)