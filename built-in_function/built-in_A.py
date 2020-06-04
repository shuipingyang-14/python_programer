# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/29 14:46
@ file:     built-in_A.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


def abs_test(num):
    """
    计算num的绝对值
    :param num: 数字
    :return: num绝对值
    """
    return abs(num)


def all_test(iter):
    """
    判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE
    :param iter: 元组或列表
    :return: True或者False
    """
    return all(iter)


def any_test(iter):
    """
    判断给定的可迭代参数 iterable 是否全部为 False
    :param iter: 元组或列表
    :return: True或者False
    """
    return any(iter)

def ascii_test(str):
    """
    返回一个表示对象的字符串
    :return:
    """
    return ascii(str)


if __name__ == '__main__':
    num = -45
    print(abs_test(num))
    num = 100.12
    print(abs_test(num))
    num = 119
    print(abs_test(num))

    l = ['1', '2', '3']  # 列表list，元素都不为空或0
    print(all_test(l))  # True
    l = ['1', '', '2']  # 列表list，存在一个为空的元素
    print(all_test(l))  # False
    l = [1, 2, 3, 0]  # 列表list，存在一个为0的元素
    print(all_test(l))  # False
    t = ('a', 'b', 'c', 'd')  # 元组tuple，元素都不为空或0
    print(all_test(t))  # True
    t = ('a', 'b', '', 'd')  # 元组tuple，存在一个为空的元素
    print(all_test(t))  # False
    t = (0, 1, 2, 3)  # 元组tuple，存在一个为0的元素
    print(all_test(t))  # False
    l = []  # 空列表
    print(all_test(l))  # True
    t = ()  # 空元组
    print(all_test(l))  # True

    l = ['1', '2', '3']  # 列表list，元素都不为空或0
    print(any_test(l))  # True
    l = ['1', '', '2']  # 列表list，存在一个为空的元素
    print(any_test(l))  # True
    l = [0, '', False]  # 列表list,元素全为0,'',false
    print(any_test(l))  # False
    t = ('a', 'b', 'c', 'd')  # 元组tuple，元素都不为空或0
    print(any_test(t))  # True
    t = ('a', 'b', '', 'd')  # 元组tuple，存在一个为空的元素
    print(any_test(t))  # True
    t = (0, '', False)  # 元组tuple，元素全为0,'',false
    print(any_test(t))  # False
    l = []  # 空列表
    print(any_test(l))  # False
    t = ()  # 空元组
    print(any_test(l))  # False

    s = "hello"
    print(ascii_test(s))
    s = 1
    print(ascii_test(s))
    s = '中国'
    print(ascii_test(s))
    s = [1,2,3,4,5]
    print(ascii_test(s))

