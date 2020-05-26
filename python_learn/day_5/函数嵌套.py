# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/26 10:17
@ file:     函数嵌套.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

def fun1():
    print("in fun1")
    print(3)

def fun2():
    print("in fun2")
    print(4)

def func3():
    print('in func3')
    print(3)

def func4():
    print('in func4')
    func3()
    print(4)

def fun5():
    print(2)
    def fun6():
        print(6)
    print(4)
    fun6()
    print(8)

if __name__ == '__main__':
    # fun1()   # in fun1   3
    # print(1)   # 1
    # fun2()  # in fun2    4
    # print(2)   # 2
    # print(1)   # 1
    # func4()   # in fun4  in fun3  3  4
    # print(2)   # 2
    print(3)  # 3
    fun5()   # 2 4 6 8
    print(5)  # 5