# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/8 13:58
@ file:     built-in_I.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

def id_test():
    """
    返回对象唯一标识符
    :return:
    """
    a = "hello"
    print(id(a))   # 2017188377968

    b = 1
    print(id(b))  # 140718175295136

    c = [1,2,3]
    print(id(c))   # 2017188389120

def input_test():
    """
    输入数据，返回字符串
    :return:
    """
    a = input("input:")   # 输入整数
    print(a)
    print(type(a))

    b = input("input:")   # 输入字符串
    print(b)
    print(type(b))

def int_test():
    """
    将一个字符串或数字转换为整型
    :return:
    """
    print(int())
    print(int(3))
    print(int(3.6))
    print(int('10', 2))
    print(int('0xa',16))
    print(int('12',16))

if __name__ == '__main__':
    id_test()
    # input_test()
    int_test()
