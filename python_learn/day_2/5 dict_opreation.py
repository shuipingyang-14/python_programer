# -*- coding: utf-8 -*-
# @Time    : 2020/5/9 21:05
# @python  : python 3.7
# @Author  : 水萍
# @File    : 5 dict_opreation.py
# @Software: PyCharm


# 1.创建字典
dic = dict((('a', 1), ('b', 2), ('c', 3)))
print(dic)

dic = dict(a=1, b=2, c=3)
print(dic)

dic = dict({'a': 1, 'b': 2, 'c': 3})
print(dic)

# 2.增加元素
d = {}
d.update(d=4)
d1 = {'a': 1, 'b': 2, 'c': 3}
d1['d'] = 5
print(d1)
# setdefault:有则不变，无则增加
d.setdefault('hello')
print(d)
d.setdefault('hello', 1)
print(d)
d.setdefault('world', 2)
print(d)

# 3.删除数据
d = {'a': 1, 'b': 2, 'c': 3}
d.pop('c')  # 按照键值删除，有返回值
d.pop('a', "no key")  # 设置第二个参数无论字典是否有此键值，都不会报错，返回值是设置的参数
d.pop('d', "no key")
print(d)
d.update({'a': 4, 'e': 2, 'f': 3})
print(d)

d.clear()  # 清空元素
print(d)

d = {'a': 1, 'b': 2, 'c': 3}
del d['a']
print(d)
# del d['d']
# print(d)

# 4.改元素
d = {'a': 1, 'b': 2, 'c': 3}
d['a'] = 4
print(d)
d.update(a=5)
print(d)

# 5.查元素
d = {'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3]}
print(d['a'])
print(d['d'][1])
res = d.get('d')
print(res)
res = d.get('e', "no key")  # 可设置返回值
print(res)

# 6.keys()
d = {'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3]}
print(d.keys(), type(d.keys()))
# 可转化成列表
print(list(d.keys()), type(list(d.keys())))
for key in dic.keys():
    print(key)

# 7.values()
d = {'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3]}
print(d.values(), type(d.values()))
print(list(d.values()), type(list(d.values())))
for value in dic.values():
    print(value)

# 8.items()
d = {'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3]}
for i, j in d.items():
    print(i, j)

# 10.fromkeys
dic = dic.fromkeys([1, 2, 3], [])  # 值共有一个，更改一个则所有值均更改
dic[1].append(666)
print(dic)  # {1: [666], 2: [666], 3: [666]}

dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'age': 18}
# 删除字典中包含k的键值对
for key in list(dic.keys()):
    if 'k' in key:
        dic.pop(key)
print(dic)
