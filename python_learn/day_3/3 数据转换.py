# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/25 16:29
@ file:     3 数据转换.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# 1. int bool str转换
# int -> bool
i = 100
print(bool(i))  # True，非零就是True
i1 = 0
print(bool(i1))  # False

# bool -> int
t = True
print(int(t))  # 1
t1 = False
print(int(t1))  # 0

# int -> str
i = 100
print(str(i))  # '100'

# str -> int
s = "100"
print(int(s))  # 100

# str -> bool
s1 = 'hello'
s2 = ''
print(bool(s1))  # True  非空就是True
print(bool(s2))  # False

# bool -> str
t1 = True
print(str(t1))  # 'True'

# 2. str list 转换
# str -> list
s1 = 'hello world'
print(s1.split())  # ['hello', 'world']

# list -> str
l1 = ['alex', 'hello', 'world']
print(" ".join(l1))  # "alex hello world"

# 3. list set转换
# list -> set
l1 = [1, 2, 3, 3]
print(set(l1))  # {1, 2, 3}

# set -> list
l1 = {1, 2, 3, 3, 4, 4}
print(list(l1))  # [1, 2, 3, 4]

# 4. str bytes转换
# str -> bytes
s1 = '你好'
print(s1.encode('utf-8'))  # b'\xe4\xbd\xa0\xe5\xa5\xbd'

# bytes -> str
s1 = b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(s1.decode('utf-8'))

# 所有数据都可以转换为bool值
# bool转换为False的值：'', 0, (), {}, [], set(), None
