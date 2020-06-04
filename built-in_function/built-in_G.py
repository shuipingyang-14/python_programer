# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/4 11:12
@ file:     built-in_G.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


def getattr_test():
    """
    返回对象属性值
    :return:
    """

    class A(object):
        bar = 1

    a = A()
    print(getattr(a, 'bar'))  # 获取属性值bar值
    # print(getattr(a, 'bar2'))  # 属性 bar2 不存在，触发异常
    print(getattr(a, 'bar2', 3))  # 属性 bar2 不存在，设置默认值


def global_test():
    """
    以字典类型返回当前位置全部全局变量
    :return:
    """
    a = 'hello'
    print(globals())  # globals 函数返回一个全局变量的字典，包括所有导入的变量


if __name__ == '__main__':
    getattr_test()
    global_test()
