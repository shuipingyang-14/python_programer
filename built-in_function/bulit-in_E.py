# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/3 16:55
@ file:     bulit-in_E.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

def enumerate_test():
    """
    enumerate测试
    :return:
    """
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    print(list(enumerate(seasons)))
    # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    print(list(enumerate(seasons, start=1)))  # 下标从 1 开始
    # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

    # 普通for循环
    seq = ['one', 'two', 'three']
    i = 0
    for element in seq:
        print(i, element)
        i+= 1

    # 使用enumerate循环
    for i, elem in enumerate(seq):
        print(i, elem)

def eval_test():
    """
    执行表达式
    :return:
    """
    x = 3
    print(eval('3*x'))
    print(eval('pow(2,2)'))

def execfile_test():
    """
    执行文件
    :return:
    """
    # execfile('bulit-in_A.py')
    pass

if __name__ == '__main__':
    enumerate_test()
    eval_test()
    # execfile_test()