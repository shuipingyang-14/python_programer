# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/19 9:48
@ file:     闭包函数.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# 内部函数包含对外部作用域而非全剧作用域名字的引用，该内部函数称为闭包函数
# 函数内部定义的函数称为内部函数

def func():
    name = 'eva'
    def inner():
        print(name)
    return inner

f = func()
f()

# 判断闭包函数
# 输出的__closure__是否有cell元素：有cell是闭包函数

def func():
    name = 'hello'
    def inner():
        print(name)
    print(inner.__closure__)
    return inner

f = func()
f()

#输出的__closure__为None ：不是闭包函数
name = 'egon'
def func2():
    def inner():
        print(name)
    print(inner.__closure__)
    return inner

f2 = func2()
f2()

# 闭包嵌套
def wrapper():
    money = 1000
    def func():
        name = 'hello'
        def inner():
            print(name, money)
        return inner
    return func

f = wrapper()
i = f()
i()

# 闭包函数获取网络
from urllib.request import urlopen

def index():
    url = "http://www.baidu.com"
    def get():
        return urlopen(url).read()
    return get

xiaohua = index()
content = xiaohua()
print(content)