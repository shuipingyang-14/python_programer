# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/16 15:45
@ file:     built-in_O.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


def oct_test():
    """
    将一个整数转换为8进制字符串
    :return:
    """
    print(oct(10))  # 0o12
    print(oct(15))  # 0o17


def open_test():
    """
    打开文件进行操作
    :return:
    """
    f = open('test.txt')
    print(f.read())


def ord_test():
    """
    把字符串转换为对应的ASCII数值
    :return:
    """
    print(ord('a'))
    print(ord('€'))


if __name__ == '__main__':
    oct_test()
    open_test()
    ord_test()
