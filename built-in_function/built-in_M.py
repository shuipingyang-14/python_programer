# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/15 10:04
@ file:     built-in_M.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


def map_test():
    """
    对指定序列做映射
    :return:
    """

    def square(x):  # 计算平方数
        return x ** 2

    res = map(square, [1, 2, 3, 4, 5])  # [1,4,9,16,25]
    print(list(res))
    print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))

    # 提供了两个列表，对相同位置的列表数据进行相加
    print(list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))  # [3, 7, 11, 15, 19]


def max_test():
    """
    返回给定参数最大值
    :return:
    """
    print("max(80, 100, 1000) : ", max(80, 100, 1000))  # 1000
    print("max(-20, 100, 400) : ", max(-20, 100, 400))  # 400
    print("max(-80, -20, -10) : ", max(-80, -20, -10))  # -10
    print("max(0, 100, -400) : ", max(0, 100, -400))  # 100


def memoryview_test():
    """
    返回给定参数的内存查看对象
    :return:
    """
    v = memoryview(bytearray('hello', 'utf-8'))
    print(v[1])  # 101
    print(v[-1])  # 111
    print(v[1:4])  # <memory at 0x000001D1F5C764C0>
    print(v[1:4].tobytes())  # b'ell'


def min_test():
    """
    返回给定参数最小值
    :return:
    """
    print("max(80, 100, 1000) : ", min(80, 100, 1000))  # 80
    print("max(-20, 100, 400) : ", min(-20, 100, 400))  # -20
    print("max(-80, -20, -10) : ", min(-80, -20, -10))  # -80
    print("max(0, 100, -400) : ", min(0, 100, -400))  # -400


if __name__ == '__main__':
    map_test()
    max_test()
    memoryview_test()
    min_test()
