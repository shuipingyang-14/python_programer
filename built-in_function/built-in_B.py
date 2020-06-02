# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/1 14:25
@ file:     built-in_B.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


def bin_test(num):
    """
    返回num的二进制表示
    :param num: 整数或者长整数
    :return: 二进制字符串
    """
    return bin(num)


def bool_test(num):
    """
    将给定参数转换为布尔类型
    :param num: 参数
    :return: True或者False
    """
    return bool(num)


def bytearray_test_1(num1):
    """
    返回一个新字节数组
    :param num1: 参数
    :return: 新字节数组
    """
    return bytearray(num1)


def bytearray_test_2(num1, num2):
    """
    返回一个新字节数组
    :param num1: 参数
    :param num2: 编码方式
    :return: 新字节数组
    """
    return bytearray(num1, num2)


if __name__ == '__main__':
    print(bin_test(10))  # 0b1010
    print(bin_test(-10))  # -0b1010

    print(bool_test(0))  # False
    print(bool_test(""))  # False
    print(bool_test(()))  # False
    print(bool_test([]))  # False
    print(bool_test({}))  # False
    print(bool_test(None))  # False
    print(bool_test('1'))  # True
    print(issubclass(bool, int))  # True

    print(bytearray_test_1(()))  # bytearray(b'')
    print(bytearray_test_1([1, 2, 3]))  # bytearray(b'\x01\x02\x03')
    print(bytearray_test_2('runoob', 'utf-8'))  # bytearray(b'runoob')
