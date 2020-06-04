# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/4 9:55
@ file:     built-in_F.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""
import math


def is_odd(n):
    """
    判断是否是奇数
    :param n:
    :return:
    """
    return n % 2 == 1


def is_sqr(x):
    """
    判断平方根是整数
    :param x:
    :return:
    """
    return math.sqrt(x) % 1 == 0


def filter_test():
    """
    过滤掉不符合条件的元素，返回一个迭代器对象
    :return:
    """
    # 过滤出列表中的所有奇数
    tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(tmplist)  # <filter object at 0x000002448A8D0280>
    newlist = list(tmplist)
    print(newlist)  # [1, 3, 5, 7, 9]

    # 过滤出1~100中平方根是整数的数
    tmplist = filter(is_sqr, range(1, 101))
    newlist = list(tmplist)
    print(newlist)


def float_test():
    """
    将整数和字符串转换为浮点数
    :return:
    """
    print(float(1))
    print(float(112))
    print(float(-123))
    print(float(-1.6))
    print(float('123'))
    print(float('11.3'))


def format_test():
    """
    格式化字符串
    :return:
    """
    print("{} {}".format("hello", "world"))  # 不指定顺序，按默认顺序
    print("{0} {1}".format("hello", "world"))  # 设置指定位置
    print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置

    # 设置参数
    print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
    # 通过字典设置参数
    site = {"name": "菜鸟教程", "url": "www.runoob.com"}
    print("网站名：{name}, 地址 {url}".format(**site))
    # 通过列表索引设置参数
    my_list = ['菜鸟教程', 'www.runoob.com']
    print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

    # 传入对象
    class Test(object):
        def __init__(self, value):
            self.value = value

    my_value = Test(6)
    print('value 为: {0.value}'.format(my_value))  # "0" 是可选的
    print('value 为: {.value}'.format(my_value))

    # 数字格式化
    print("{:.2f}".format(3.1415926))  # 3.14  不带符号保留小数点后两位
    print("{:+.2f}".format(3.1415926))  # + 3.14  带符号保留小数点后两位
    print("{:+.2f}".format(-1))  # -1.00  	带符号保留小数点后两位
    print("{:.2%}".format(0.25))  # 25.00%	百分比格式
    print("{:.2e}".format(1000000000))  # 1.00e+09	指数表示

    # 转义{}
    print("{} 对应的位置是 {{0}}".format("runoob"))  # runoob 对应的位置是 {0}


def frozenset_test():
    """
    返回冻结集合
    :return:
    """
    res = frozenset()
    print(res)  # frozenset()

    res = frozenset(range(10))
    print(res)  # frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})

    res = frozenset('runoob')
    print(res)  # frozenset({'r', 'o', 'u', 'n', 'b'})


if __name__ == '__main__':
    filter_test()
    float_test()
    format_test()
    frozenset_test()
