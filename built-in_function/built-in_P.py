# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/17 16:04
@ file:     built-in_P.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


def pow_test():
    """
    返回x的y次方的值
    :return:
    """
    import math

    print("math.pow(100, 2) : ", math.pow(100, 2))  # 10000.0
    # 使用内置，查看输出结果区别
    print("pow(100, 2) : ", pow(100, 2))  # 10000
    print("math.pow(100, -2) : ", math.pow(100, -2))  # 0.0001
    print("math.pow(2, 4) : ", math.pow(2, 4))  # 16.0
    print("math.pow(3, 0) : ", math.pow(3, 5))  # 243.0
    print("pow(3, 5, 4) : ", pow(3, 5, 4))  # 243%4 = 3


def print_test():
    """
    打印输出
    :return:
    """

    import time

    print(1)
    print("Hello World")

    a = 1
    b = 'runoob'
    print(a, b)

    print("aaa""bbb")
    print("aaa", "bbb")

    print("www", "runoob", "com", sep=".")  # 设置间隔符


    print("---Loading 效果---")

    print("Loading", end="")
    for i in range(10):
        print(".", end='', flush=True)
        time.sleep(0.2)


def property_test():
    """
    在新式类中返回属性值
    :return:
    """
    class C(object):
        def __init__(self):
            self._x = None

        def getx(self):
            return self._x

        def setx(self, x):
            self._x = x

        def delx(self):
            del self._x

        x = property(getx, setx, delx, "I'm the 'x' property.")
        print(x)

if __name__ == '__main__':
    pow_test()
    print_test()
    property_test()
