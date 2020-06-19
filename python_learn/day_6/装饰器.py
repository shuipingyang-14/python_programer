# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/19 10:02
@ file:     装饰器.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

import time

def timer(func):
    def inner():
        start = time.time()
        func()
        print(time.time() - start)
    return inner

@timer  #==> fun1 = timer(fun1)
def fun1():
    print("in func1...")


fun1()

# 装饰器的本质：一个闭包函数
# 装饰器的功能：在不修改原函数及其调用方式的情况下对原函数功能进行扩展


# 装饰带一个参数的函数
def timer(func):
    def inner(a):
        start = time.time()
        func(a)
        print(time.time() - start)
    return inner

@timer
def fun1(a):
    print(a)

fun1(1)

# 装饰好多参数的函数
def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        re = func(*args, **kwargs)
        print(time.time() - start)
        return re
    return inner

@timer   #==> func1 = timer(func1)
def func1(a,b):
    print(a, b)
    print('in func1...')

@timer   #==> func2 = timer(func2)
def func2(a):
    print('in func2 and get a:%s'%(a))
    print("in fun2...")

func1('aaaaaa','bbbbbb')
func2('aaaaaa')

# 带返回的装饰器
def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        re = func(*args, **kwargs)
        print(time.time() - start)
        return re
    return inner

@timer   #==> func1 = timer(func1)
def func1(a,b):
    print(a, b)
    print('in func1...')

@timer   #==> func2 = timer(func2)
def func2(a):
    print('in func2 and get a:%s'%(a))
    return "fun2"

func1('aaaaaa','bbbbbb')
print(func2('aaaaaa'))

# 查看函数信息方法
def index():
    '''这是一个主页信息'''
    print("from index")

print(index.__doc__)    #查看函数注释的方法
print(index.__name__)   #查看函数名的方法

from functools import wraps

def demo(func):
    @wraps(func)  #加在最内层函数正上方
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper

@demo
def index():
    '''这是一个主页信息'''
    print("from index")

print(index.__doc__)    #查看函数注释的方法
print(index.__name__)   #查看函数名的方法

# 装饰器的主要功能：
#  在不改变函数调用方式的基础上在函数的前、后添加功能

# 装饰器的固定格式：
def timer(func):
    def inner(*args,**kwargs):
        '''执行函数之前要做的'''
        re = func(*args,**kwargs)
        '''执行函数之后要做的'''
        return re
    return inner

from functools import wraps

def deco(func):
    @wraps(func) #加在最内层函数正上方
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper

# 带参数的装饰器
def outer(flag):
    def timer(func):
        def inner(*args, **kwargs):
            if flag:
                print("执行函数前要做的")
                start = time.time()
            re = func(*args, **kwargs)
            if flag:
                print("执行函数之后要做的")
                print(time.time() - start)
            return re
        return inner
    return timer

@outer(False)
def func():
    print(111)

func()

@outer(1)
def func():
    print(111)

func()

# 多个装饰器装饰同一个函数
def wrapper1(func):
    def inner():
        print('wrap1,before func')
        func()
        print('wrap1, after func')
    return inner

def wrapper2(func):
    def inner():
        print('wrap2,before func')
        func()
        print('wrap2, after func')
    return inner

@wrapper1
@wrapper2
def f():
    print('in f...')

f()