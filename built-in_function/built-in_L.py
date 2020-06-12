# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/11 13:11
@ file:     built-in_L.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


def len_test():
    """
    返回对象长度
    :return:
    """
    str = "hello world"
    print(len(str))

    l = [1, 2, 3]
    print(len(l))

    d = {"1": 1, "2": 2, "3": 3}
    print(len(d))


def list_test():
    """
    将元组或字符串转换为列表
    :return:
    """
    t = (1, 'hello', '4')
    l = list(t)
    print("列表元素：", l)

    str = "Hello World"
    list2 = list(str)
    print("列表元素 : ", list2)


def locals_test():
    """
    以字典形式返回当前所有局部变量
    :return:
    """

    def runoob(arg):  # 两个局部变量：arg、z
        z = 1
        print(locals())  # {'arg': 4, 'z': 1}

    runoob(4)


if __name__ == '__main__':
    len_test()
    list_test()
    locals_test()
