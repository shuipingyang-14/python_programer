# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/26 10:31
@ file:     函数使用.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


# 1. 函数内存地址
def func():
    print("呵呵")


print(func)  # 结果: <function func at 0x1101e4ea0>


# 函数名指向的是这个函数的内存地址
# 函数内存地址()执行这个函数

# 2. 函数名赋值
def func():
    print("呵呵")


a = func  # 把函数当作一个变量赋值给另一个变量
a()  # 函数调用func()

# 3. 函数名可以当作容器类的元素
a = 1
b = 'alex'
c = '你好'
l1 = [a, b, c]
for i in l1:
    print(i)


def fun1():
    print("in fun1...")


def fun2():
    print("in fun2...")


def fun3():
    print("in fun3...")


def fun4():
    print("in fun4...")


l1 = [fun1, fun2, fun3, fun4]
for i in l1:
    i()


# 4. 函数名可以当作函数参数
def fun1():
    print("in fun1...")


def fun2(f):
    print("in fun2...")
    f()


fun2(fun1)  # in fun2...   in fun1...


# 5. 函数名可以作为函数返回值
def func1():
    print('in func1')


def func2(f):
    print('in func2')
    return f


ret = func2(func1)
ret()  # ret, f, func1 都是指向的func1这个函数的内存地址
