# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/25 18:56
@ file:     4 函数参数.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


# 1. 动态参数
# ​ 动态接收位置参数：*args
# *args，会将实参所有的位置参数接收，放置在一个元组中，并将这个元组赋值给args这个形参
def eat(*args):
    print("我请你吃：", args)


def my_max(*args):
    n = 0
    for i in args:
        n += i
    return n


# 动态接收关键字参数: **kwargs
# **kwargs，是接受所有的关键字参数然后将其转换成一个字典赋值给kwargs这个形参
def func(*args, **kwargs):
    print(args)
    print(kwargs)


def func_1(*args):
    print(args)  # ('a', 'l', 'e', 'x', 1, 2, 3, 4, '武sir', '太白', '女神')


def func_2():
    # 处理剩下元素
    # 之前讲过的分别赋值
    a, b = (1, 2)
    print(a, b)  # 1 2
    # 其实还可以这么用：
    a, *b = (1, 2, 3, 4,)
    print(a, b)  # 1 [2, 3, 4]
    *rest, a, b = range(5)
    print(rest, a, b)  # [0, 1, 2] 3 4
    print([1, 2, *[3, 4, 5]])  # [1, 2, 3, 4, 5]


# 参数传递顺序：位置参数，*args，默认参数，**kwargs
def func_3(a, b, *args, c):
    print(a, b)  # 1 2
    print(args)  # (3, 4)
    print(c)


# 形参角度的所有形参的最终顺序为：位置参数，*args，默认参数，仅限关键字参数，**kwargs
def foo(a, b, *args, c, sex=None, **kwargs):
    print(a, b, c, sex, args, kwargs)


if __name__ == '__main__':
    # eat('蒸羊羔儿','蒸熊掌','蒸鹿尾儿','烧花鸭','烧雏鸡','烧子鹅')
    # sum = my_max(1,2,3,4,5,6,7,8,9,10)
    # print(sum)
    # func('蒸羊羔儿','蒸熊掌','蒸鹿尾儿','烧花鸭','烧雏鸡','烧子鹅',name='太白金星',sex='男')
    # s1 = 'alex'
    # l1 = [1, 2, 3, 4]
    # tu1 = ('武sir', '太白', '女神',)
    # func_1(*s1, *l1, *tu1)
    # dic1 = {'name': '太白', 'age': 18}
    # dic2 = {'hobby': '喝茶', 'sex': '男'}
    # func(*tu1, **dic1, **dic2)
    # func_3(1, 2, 3, 4, c=5)

    # foo(1,2,3,4,c=6)
    # foo(1,2,sex='男',name='alex',hobby='old_woman')
    # foo(1,2,3,4,name='alex',sex='男')
    # foo(1,2,c=18)
    # foo(2, 3, [1, 2, 3],c=13,hobby='喝茶')
    foo(*[1, 2, 3, 4], **{'name': '太白', 'c': 12, 'sex': '女'})
