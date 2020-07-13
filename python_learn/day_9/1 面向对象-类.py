# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/9 14:55
@ file:     1 面向对象-类.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# 面向对象编程 测量对象的元素个数
s1 = "hello world"
count = 0
for i in s1:
    count += 1
print(count)

l1 = [1, 2, 3, 4]
count = 0
for i in l1:
    count += 1
print(count)


def func(s):
    count = 0
    for i in s:
        count += 1
    return count


print(func("hello world"))
print(func([1, 2, 3, 4]))

# 面向对象编程的特点:
"""
a. 减少代码重用性
b. 增强代码可读性
"""


# 函数式编程
# auth 认证相关
def login():
    pass


def resister():
    pass


# account相关
def func1():
    pass


def fun2():
    pass


# 购物车相关
def shopping(username, money):
    pass


def check_paidgoods(username, money):
    pass


def check_unpaidgoods(username, money):
    pass


def save(username, money):
    pass


# 面向对象编程
class LoginHalder:
    def login(self):
        pass

    def resister(self):
        pass


class Account:
    def func1(self):
        pass

    def func2(self):
        pass


class ShoppingCar:
    def shopping(username, money):
        pass

    def check_paidgoods(username, money):
        pass

    def check_unpaidgoods(username, money):
        pass

    def save(username, money):
        pass

# 类的结构
class Human:
    """
    构建人类
    """
    mind = '有思想' # 静态属性 属性 静态变量 静态字段
    dic = {}
    l1 = {}
    def work(self): # 方法，函数，动态属性
        print('人类会工作')

    def tools(self):
        print('人类会使用工具')

# 类名操作静态属性
# 查看类中的所有内容：类名.__dict__方式：只能查询，不能增删改.
print(Human.__dict__)
# {'__module__': '__main__', '__doc__': '\n    构建人类\n    ', 'mind': '有思想', 'dic': {}, 'l1': {}, 'work': <function Human.work at 0x000002C025F22C10>, '__dict__': <attribute '__dict__' of 'Human' objects>, '__weakref__': <attribute '__weakref__' of 'Human' objects>}
print(Human.__dict__['mind'])
# 有思想

# 万能点
print(Human.mind)  # 查
# 有思想
Human.mind = '无脑'  # 改
print(Human.mind)
# 无脑
del Human.mind  # 删
Human.walk = '直立行走'
print(Human.walk)
# 直立行走
# 通过万能的点 可以增删改查类中的单个属性

# 类名操作动态方法
Human.work(111)
# 人类会工作
Human.tools(111)
# 人类会使用工具