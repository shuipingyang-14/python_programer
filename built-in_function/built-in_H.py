# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/4 17:31
@ file:     built-in_H.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


def hasattr_test():
    """
    判断对象是否包含对应的属性
    :return:
    """

    class Coordinate:
        x = 10
        y = -5
        z = 0

    point1 = Coordinate()
    print(hasattr(point1, 'x'))  # True
    print(hasattr(point1, 'y'))  # True
    print(hasattr(point1, 'z'))  # True
    print(hasattr(point1, 'no'))  # False  没有该属性


def hash_test():
    """
    返回对象的哈希值
    :return:
    """
    res = hash('test')  # 字符串
    print(res)  # 2253931735421975283
    res = hash(1)  # 数字
    print(res)  # 1
    res = hash(str([1, 2, 3]))  # 集合
    print(res)  # 4398412502669230547
    res = hash(str(sorted({'1': 1})))  # 字典
    print(res)  # 8831821087711437813


def help_test():
    """
    查看函数或者模块用途的详细说明
    :return:
    """
    print(help('sys'))
    print(help('str'))
    a = [1, 2, 3]
    print(help(a))
    print(help(a.append))


def hex_test():
    """
    将一个数字转换为16进制数
    :return:
    """
    print(hex(255))  # 0xff
    print(hex(-42))  # 0x2a
    print(hex(12))  # 0xc
    print(type(hex(255)))  # <class 'str'>


if __name__ == '__main__':
    hasattr_test()
    hash_test()
    help_test()
    hex_test()
