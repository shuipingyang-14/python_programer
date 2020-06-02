# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/29 9:54
@ file:     最大几个数.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

def max_num(nums, k):
    # temp = []
    # inf = 0
    # for i in range(k):
    #     temp.append(max(nums))
    #     nums.pop(nums.index(max(nums)))
    # return temp
    nums.sort()
    temp = []
    for i in range(k):
        temp.append(nums[i])
    return temp

def get_greatest_numbers(nums, k):
    num = [0]*10000
    for a in nums:
        num[a] += 1   # 对重复元素计数
    print(num)
    output = []
    i = len(num)-1  # 从最后遍历(最大值)
    while len(output) < k:
        if num[i] >= 1:  # 如果该索引处的值大于1，则说明该值存在至少1次，循环往output里面写
            for j in range(num[i]):
                output.append(i)
        i -= 1
    return output[:k]


if __name__ == '__main__':
    nums = [1, 8, 2, 23, 7, 4, 18, 23, 24, 37, 2]
    res = max_num(nums, 3)
    print(res)
    # nums = [1, 8, 2, 23, 7, -4, 18, 23, 23, 37, 2]
    # res = max_num(nums, 3)
    # print(res)
    # res = get_greatest_numbers(nums, 3)
    # print(res)