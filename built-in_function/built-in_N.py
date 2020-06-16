# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/15 11:11
@ file:     built-in_N.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

def next_test():
    """
    返回迭代器的下一项信息
    :return:
    """

    # 首先获得Iterator对象:
    it = iter([1, 2, 3, 4, 5])
    # 循环:
    while True:
        try:
            # 获得下一个值:
            x = next(it)
            print(x)
        except StopIteration:
            # 遇到StopIteration就退出循环
            break

if __name__ == '__main__':
    next_test()