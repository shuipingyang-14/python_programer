# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/23 10:05
@ file:     built-in_Z.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


def zip_test():
    """
    将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组
    :return:
    """
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [4, 5, 6, 7, 8]

    zipped = zip(a, b)  # 返回一个对象
    print(zipped)  # <zip object at 0x0000017FBE509500>
    print(list(zipped))  # list() 转换为列表
    # [(1, 4), (2, 5), (3, 6)]
    print(list(zip(a, c)))  # 元素个数与最短的列表一致
    # [(1, 4), (2, 5), (3, 6)]
    a1, a2 = zip(*zip(a, b))  # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
    print(list(a1))  # [1, 2, 3]
    print(list(a2))  # [4, 5, 6]


if __name__ == '__main__':
    zip_test()
