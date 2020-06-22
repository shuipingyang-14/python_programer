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

    res = tuple({1:2,3:4}) # 针对字典 会返回字典的key组成的tuple
    print(res)

    res = tuple((1,2,3,4))    #元组会返回元组自身
    print(res)

    aList = [123, 'xyz', 'zara', 'abc']
    aTuple = tuple(aList)

    print("Tuple elements : ", aTuple)

if __name__ == '__main__':
    tuple_test()