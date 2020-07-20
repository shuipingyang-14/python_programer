# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/18 20:19
@ file:     process_test.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

from multiprocessing import Process
import os


def func():
    print(os.getpid(), os.getppid())


print(123)
if __name__ == '__main__':
    p = Process(target=func)
    p.start()
