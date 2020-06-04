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
    print(getattr(a, 'bar'))   # 获取属性值bar值
    # print(getattr(a, 'bar2'))  # 属性 bar2 不存在，触发异常
    print(getattr(a, 'bar2', 3))  #  属性 bar2 不存在，设置默认值


if __name__ == '__main__':
    getattr_test()