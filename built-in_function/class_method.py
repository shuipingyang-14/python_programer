# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/22 17:11
@ file:     class_method.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


class TestFunc(object):
    def instance_func(self, x):
        print('instance_func(%s, %s)' % (self, x))

    @classmethod
    def class_func(cls, x):
        print('class_func(%s, %s)' % (cls, x))

    @staticmethod
    def static_func(x):
        print('static_fuc(%s)' % x)


test_func = TestFunc()

# 实例方法
test_func.instance_func(1)  # instance_func(<__main__.TestFunc object at 0x000002757D1001C0>, 1)
# 类方法
test_func.class_func(1)  # class_func(<class '__main__.TestFunc'>, 1)
TestFunc.class_func(1)  # class_func(<class '__main__.TestFunc'>, 1)
# 静态方法
test_func.static_func(1)  # static_fuc(1)
TestFunc.static_func(1)  # static_fuc(1)

import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():  # Data.now()产生实例，实例使用当前时间
        t = time.localtime()  # 获取结构化时间格式
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    @staticmethod
    def tomorrow():  # Data.now()产生实例，实例使用明天时间
        t = time.localtime(time.time() + 86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    def now_1(self):  # Data.now()产生实例，实例使用当前时间
        t = time.localtime()  # 获取结构化时间格式
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    def tomorrow_1(self):  # Data.now()产生实例，实例使用明天时间
        t = time.localtime(time.time() + 86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    @classmethod
    def now_2(cls):  # Data.now()产生实例，实例使用当前时间
        t = time.localtime()  # 获取结构化时间格式
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    @classmethod
    def tomorrow_2(cls):  # Data.now()产生实例，实例使用明天时间
        t = time.localtime(time.time() + 86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)


# staticmethod不实例化
a = Date('1987', 11, 27)  # 自己定义时间
b = Date.now()  # 采用当前时间
c = Date.tomorrow()  # 采用明天的时间

print(a.year, a.month, a.day)  # 1987 11 27
print(b.year, b.month, b.day)  # 2020 6 22
print(c.year, c.month, c.day)  # 2020 6 23

# staticmethod实例化
a = Date('1987', 11, 27)  # 自己定义时间
b = Date.now()  # 采用当前时间
c = Date.tomorrow()  # 采用明天的时间

print(a.year, a.month, a.day)  # 1987 11 27
print(b.year, b.month, b.day)  # 2020 6 22
print(c.year, c.month, c.day)  # 2020 6 23

# instance实例化
a = Date('1987', 11, 27)  # 自己定义时间
b = a.now_1()  # 采用当前时间
c = a.tomorrow_1()  # 采用明天的时间

print(a.year, a.month, a.day)  # 1987 11 27
print(b.year, b.month, b.day)  # 2020 6 22
print(c.year, c.month, c.day)  # 2020 6 23

# classmethod不实例化
a = Date('1987', 11, 27)  # 自己定义时间
b = Date.now_2()  # 采用当前时间
c = Date.tomorrow_2()  # 采用明天的时间

print(a.year, a.month, a.day)  # 1987 11 27
print(b.year, b.month, b.day)  # 2020 6 22
print(c.year, c.month, c.day)  # 2020 6 23

# classmethod实例化
a = Date('1987', 11, 27)  # 自己定义时间
b = a.now_2()  # 采用当前时间
c = a.tomorrow_2()  # 采用明天的时间

print(a.year, a.month, a.day)  # 1987 11 27
print(b.year, b.month, b.day)  # 2020 6 22
print(c.year, c.month, c.day)  # 2020 6 23


# 继承类的区别
# 子类实例继承父类static_method静态方法，调用方法，还是调用父类的方法和类属性
# 子类实例继承父类class_method类方法，调用方法，调用的是子类的方法和子类的类属性

class Foo(object):
    X = 1
    Y = 2

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / 1

    @staticmethod
    def static_method():
        return Foo.averag(Foo.X, Foo.Y)

    @classmethod
    def class_method(cls):
        return cls.averag(cls.X, cls.Y)


class Son(Foo):
    X = 3
    Y = 5

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / 2

p = Son()
print(p.static_method()) # 3.0
print(p.class_method()) # 4.0
