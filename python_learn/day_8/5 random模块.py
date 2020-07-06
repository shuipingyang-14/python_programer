# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/2 13:38
@ file:     5 random模块.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

import random

# 1. random()获取[0.0, 1.0]之阿健的浮点数
print(random.random())  # 0.38633156120825607

# 2. uniform(a, b)获取[a, b]之间的浮点数
print(random.uniform(4,10))  # 9.88703148684846

# 3. randint(a, b)获取[a, b]之间的整数
print(random.randint(4,10))   # 4

# 4. 大于等于1小于10之间的奇数
print(random.randrange(1, 10, 2))  # 7
# 大于等于1小于10之间的偶数
print(random.randrange(2, 10, 2))  # 6

# 5. 打乱排序
lst = list(range(10))
random.shuffle(lst)
print(lst)  # [2, 8, 4, 5, 6, 9, 7, 1, 0, 3]

# 6. sample(x, k)从x中随机抽取k个数据，组成列表返回
t = (1,2,3,4,5,6,7,8,9)
print(random.sample(t, 4))  # [5, 7, 2, 6]
print(random.sample(t, len(t)))   # [6, 7, 9, 2, 5, 8, 4, 3, 1]

# 7. 随机选择一个返回
print(random.choice([1, '23', [4,5]]))  # 1或者23或者[4,5]
# 23
print(random.sample([1, '23', [4, 5]], 2))  # 列表元素任意2个组合
# [[4,5], '23']

# 生成随机验证码
def v_code():
    code=''
    for i in range(5):
        num = random.randint(0, 9)
        alf = chr(random.randint(65, 90))
        add = random.choice([num, alf])
        code="".join([code, str(add)])

    return code

print(v_code())

