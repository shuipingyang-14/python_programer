# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/14 17:55
@ file:     列表中最短的字符串.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

strs = ["flower", "flow", "flight"]
len_str = len(strs[0])
min_num_index = 0   # 最小值的下标
stack = [strs[0]]   # 利用栈来找出最短的字符串
print(stack)
for index, string in enumerate(strs):
    if len(string) < len_str:
        stack.pop()
        len_str = len(string)
        min_num_index = index # 知道最短字符对应的下标后，也可以自己找出最短字符
        stack.append(string)
print("最短字符串长度:", len_str)
print("最短字符串下标:", min_num_index)
print("最短字符串:", stack)
