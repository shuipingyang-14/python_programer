# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/1 10:45
@ file:     module_test.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

print("from the module_test.py...")
name = "xy"
__all__ = ['name', 'read1', ]


def read1():
    print("module_test模块：", name)


def read2():
    print("module_test模块")
    read1()


def change():
    global name
    name = 'ysp'
