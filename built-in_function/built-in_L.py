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

    l = [1,2,3]
    print(len(l))

    d = {"1":1, "2":2, "3":3}
    print(len(d))

if __name__ == '__main__':
    len_test()