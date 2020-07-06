# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/3 11:44
@ file:     collections模块.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# collections模块提供额外的数据类型：
"""
namedtuple：生成可以使用名字来访问元素内容的tuple
deque：双端队列，可以快速从另一端追加和推出元素
Counter：计数器，用来计数
OrderedDict：有序字典
defauledict：带有默认值的字典
"""

# 1. namedtuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)  # Point(x=1, y=2)
print(p.x)  # 1
print(p.y)  # 2

# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(1, 2, 3)
print(c)  # Circle(x=1, y=2, r=3)

# 2. deque
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)  # deque(['y', 'a', 'b', 'c', 'x'])
q.pop()
print(q)  # deque(['y', 'a', 'b', 'c'])
q.popleft()
print(q)  # deque(['a', 'b', 'c'])

# 3. OrderDict
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3), ('e', 4), ('f', 5), ('g', 6)])
print(d)  # dict的Key是无序的
# {'a': 1, 'b': 2, 'c': 3, 'e': 4, 'f': 5, 'g': 6}
od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('e', 4), ('f', 5), ('g', 6)])
print(od)  # OrderedDict的Key是有序的
# OrderedDict([('a', 1), ('b', 2), ('c', 3), ('e', 4), ('f', 5), ('g', 6)])

# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(od.keys())  # 按照插入的Key的顺序返回  odict_keys(['z', 'y', 'x'])

# 4. defaultdict
# 有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中
li = [11, 22, 33, 44, 55, 77, 88, 99, 90]
result = {}
for row in li:
    if row > 66:
        if 'key1' not in result:
            result['key1'] = []
        result['key1'].append(row)
    else:
        if 'key2' not in result:
            result['key2'] = []
        result['key2'].append(row)
print(result)  # {'key2': [11, 22, 33, 44, 55], 'key1': [77, 88, 99, 90]}

from collections import defaultdict

my_dict = defaultdict(list)
print(my_dict)  # defaultdict(<class 'list'>, {})

for value in li:
    if value > 66:
        my_dict['k1'].append(value)
    else:
        my_dict['k2'].append(value)
print(my_dict)  # defaultdict(<class 'list'>, {'k2': [11, 22, 33, 44, 55], 'k1': [77, 88, 99, 90]})

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1']) # key1存在 abc
print(dd['key2']) # key2不存在，返回默认值 N/A

# 5. Counter
# Counter类的目的是用来跟踪值出现的次数
# Counter类是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value
# 计数值可以是任意的Interger（包括0和负数）

from collections import Counter

c = Counter('abcdeabcdabcaba')
print(c) # Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})

