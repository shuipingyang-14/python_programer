# -*- coding: utf-8 -*-
# @Time    : 2020/5/10 12:45
# @python  : python 3.7
# @Author  : 水萍
# @File    : 1 copy_opreation.py
# @Software: PyCharm


# 赋值运算
l1 = [1,2,3,[22,33]]
l2 = l1
l2.append(6)
print(l1)
print(l2)

# 浅copy: 在内存中新开辟一个空间，存放copy的列表，但列表里面的内容还是沿用之前对象的内存地址，所L1,L2的id不，但是内容id是一样的
l1 = [1,2,3,[22,33]]
l2 = l1.copy()
l2.append(6)
print(l1, id(l1))
print(l2, id(l2))

l1 = [1,2,3,[22,33]]
l2 = l1.copy()
l2[-1].append(6)
print(l1, id(l1[-1]))
print(l2, id(l2[-1]))


# 深拷贝：深拷贝将数据类型在内存中重新创建一份，不可变的数据类型沿用之前的内存地址
import copy
l1 = [1,2,3,[22,33]]
l2 = copy.deepcopy(l1)
print(id(l1))
print(id(l2))
l1[-1].append(44)
print(id(l1[-1]))
print(id(l2[-1]))
print(l1)
print(l2)
print(id(l1[0]))
print(id(l2[0]))

l1 = [1,2,3,[22,33]]
l2 = l1[:]  # 相当于浅拷贝
l1[-1].append(666)
print(l1)
print(l2)

# 浅拷贝：嵌套的可变的数据类型是同一个
# 深拷贝：嵌套的可变的数据类型不是同一个