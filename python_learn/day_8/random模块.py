# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/2 13:38
@ file:     random模块.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

import random

# random()获取[0.0, 1.0]之阿健的浮点数
print(random.random())  # 0.38633156120825607

# uniform(a, b)获取[a, b]之间的浮点数
print(random.uniform(4,10))  # 9.88703148684846

# randint(a, b)获取[a, b]之间的整数
print(random.randint(4,10))   # 4

# 打乱排序
lst = list(range(10))
random.shuffle(lst)
print(lst)

# sample(x, k)从x中随机抽取k个数据，组成列表返回
t = (1,2,3,4,5,6,7,8,9)
print(random.sample(t, 4))
print(random.sample(t, len(t)))

