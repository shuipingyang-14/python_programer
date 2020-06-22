# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/22 10:55
@ file:     built-in_R.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


def range_test():
    """
    返回可迭代对象
    :return:
    """
    print(range(5))  # range(0, 5)

    for i in range(5):
        print(i)

    print(list(range(5)))  # [0, 1, 2, 3, 4]
    print(list(range(0)))  # []

    print(list(range(0, 30, 5)))  # [0, 5, 10, 15, 20, 25]
    print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
    print(list(range(0, -10, -1)))  # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
    print(list(range(10, 0, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(list(range(1, 0)))  # []

    # range返回的结果是一个整数序列的对象，而不是列表
    print(type(range(10)))  # <class 'range'>


def repr_test():
    """
    将对象转换为供解释器读取形式，返回对象的str形式
    :return:
    """
    s = 'RUNOOB'
    print(repr(s))  # 'RUNOOB'

    dict = {'runoob': 'runoob.com', 'google': 'google.com'}
    # print(type(repr(dict)))  # <class 'str'>
    print(repr(dict))  # {'runoob': 'runoob.com', 'google': 'google.com'}


def reversed_test():
    """
    返回一个反转的迭代器
    :return:
    """
    # 字符串
    seqString = 'Runoob'
    print(reversed(seqString))
    l1 = list(reversed(seqString))
    print("".join(l1))

    # 元组
    seqTuple = ('R', 'u', 'n', 'o', 'o', 'b')
    print(reversed(seqTuple))
    print(tuple(reversed(seqTuple)))

    # range
    seqRange = range(5, 9)
    print(list(seqRange))  # [5,6,7,8]
    print(list(reversed(seqRange)))  # [8, 7, 6, 5]

    # 列表
    seqList = [1, 2, 4, 3, 5]
    print(list(reversed(seqList)))  # [5, 3, 4, 2, 1]


def round_test():
    """
    返回浮点数x的四舍五入值
    :return:
    """
    print("round(70.23456) : ", round(70.23456))  # 70
    print("round(56.651,1) : ", round(56.651, 1))  # 56.7
    print("round(56.650,1) : ", round(56.650, 1))  # 56.6
    print("round(80.264, 2) : ", round(80.264, 2))  # 80.26
    print("round(100.000056, 3) : ", round(100.000056, 3))  # 100.0
    print("round(-100.000056, 3) : ", round(-100.000056, 3))  # -100.0
    print("round(-10.675, 2) : ", round(-10.675, 2))  # -10.68
    print("round(-10.62, 1) : ", round(-10.675, 1))  # -10.7
    print("round(-10.4367, 1) : ", round(-10.4367, 1))  # -10.4


if __name__ == '__main__':
    range_test()
    repr_test()
    reversed_test()
    round_test()
