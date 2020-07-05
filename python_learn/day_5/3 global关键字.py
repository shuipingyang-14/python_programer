# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/26 10:24
@ file:     3 global关键字.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# 局部作用域对全局作用域的变量（此变量只能是不可变的数据类型）只能进行引用，而不能进行改变，只要改变就会报错
# global第一个功能：在局部作用域中可以更改全局作用域的变量(限于字符串，数字)
count = 1


def search():
    global count
    count = 2


search()
print(count)


# global第二个功能：声明全局变量
def func():
    global a
    a = 3


func()
print(a)


# 在局部作用域如果想对父级作用域的变量进行改变时，需要用到nonlocal
# 1. nonlocal不能更改全局变量
# 2. 在局部作用域中，对父级作用域（或者更外层作用域非全局作用域）的变量进行引用和修改，并且引用的哪层，从那层及以下此变量全部发生改变
def add_b():
    b = 42

    def do_global():
        b = 10
        print(b)

        def dd_nonlocal():
            nonlocal b
            b += 20
            print(b)

        dd_nonlocal()
        print(b)

    do_global()
    print(b)


add_b()
