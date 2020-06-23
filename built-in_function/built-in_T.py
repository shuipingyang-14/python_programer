# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/22 18:14
@ file:     built-in_T.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


def tuple_test():
    """
    将可迭代对象转换为元组
    :return:
    """
    res = tuple([1, 2, 3, 4])
    print(res)

    res = tuple({1: 2, 3: 4})  # 针对字典 会返回字典的key组成的tuple
    print(res)

    res = tuple((1, 2, 3, 4))  # 元组会返回元组自身
    print(res)

    aList = [123, 'xyz', 'zara', 'abc']
    aTuple = tuple(aList)

    print("Tuple elements : ", aTuple)


def type_test():
    """
    返回对象类型
    :return:
    """
    # 一个参数
    print(type(1))
    print(type('hello'))
    print([1])
    print(type({'1': 1}))
    print(type((1,)))
    print(type(1) == int)

    # 三个参数
    class X(object):
        a = 1

    X = type('X', (object,), dict(a=1))
    print(X)  # <class '__main__.X'>

    # type和isinstance区别：
    #type()不会认为子类是一种父类类型，不考虑继承关系

    #isinstance()会认为子类是一种父类类型，考虑继承关系
    class A:
        pass

    class B(A):
        pass

    print(isinstance(A(), A)) # true
    print(type(A()) == A) # true
    print(isinstance(B(), A)) # true
    print(type(B()) == A) # false


if __name__ == '__main__':
    tuple_test()
    type_test()
