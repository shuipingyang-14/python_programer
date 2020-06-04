# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/1 16:18
@ file:     built-in_C.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""
import operator


def callable_test(num):
    """
    检查一个对象是否是可调用
    :param num: 参数
    :return: 可调用返回True,否则返回False
    """
    return callable(num)


def add_test(a, b):
    """
    求两个数的和
    :param a: 参数1
    :param b: 参数2
    :return: a+b
    """
    return a + b


class A:  # 类
    def method(self):
        return 0


class B:  # 类
    def __call__(self):
        return 0


def chr_test(num):
    """
    整数对应的字符
    :param num: 整除
    :return: 整数对应的字符
    """
    return chr(num)


class A_Test(object):
    bar = 1

    def fun1(self):
        print("fun1...")

    @classmethod
    def fun2(cls):
        print('func2...')
        print(cls.bar)
        cls().fun1()  # 调用 fun1 方法


def cmp_test(a, b):
    """
    比较两数的大小
    :param a: 参数1
    :param b: 参数2
    :return: 如果x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
    """
    print(operator.gt(a, b))  # >
    print(operator.ge(a, b))  # >=
    print(operator.lt(a, b))  # <
    print(operator.le(a, b))  # <=
    print(operator.eq(a, b))  # ==


def compile_test(str1, str2, str3):
    """
    编译为字节代码对象
    :param str1: 字符串
    :param str2: 文件名称
    :param str3: 编译代码种类
    :return: 表达式执行结果
    """
    return compile(str1, str2, str3)


def complex_test_1(num1, num2=0):
    """
    创建复数
    :param num1: 整数
    :param num2：整数
    :return: 复数
    """
    return complex(num1, num2)


def complex_test_2(str):
    """
    创建复数
    :param str: 字符串
    :return: 复数
    """
    return complex(str)


if __name__ == '__main__':
    print(callable_test(0))  # False
    print(callable_test("hello"))  # False
    print(callable_test(add_test))  # 函数返回 True
    print(callable_test(A))  # 类返回 True
    print(callable_test(A()))  # 没有实现 __call__, 返回 False
    print(callable_test(B))  # 类返回True
    print(callable_test(B()))  # 实现 __call__, 返回 True

    print(chr_test(0x30))  # '0'
    print(chr_test(0x61))  # 'a'
    print(chr_test(48))  # '0'
    print(chr_test(97))  # 'a'

    A_Test.fun2()  # fun2...   1  fun1...
    # 不需要实例化

    # python 3.8不支持cmp, 用operator代替
    cmp_test(80, -100)  # False False True True False

    str = "for i in range(10):print(i)"
    c = compile_test(str, '', 'exec')  # 编译为字节代码对象
    print(c)  # <code object <module> at 0x0000020B045A9DF0, file "", line 1>
    exec(c)
    str = "3*4+5"
    c = compile_test(str, '', 'eval')  # 编译为字节代码对象
    print(c)  # <code object <module> at 0x000001AF2AD28DF0, file "", line 1>
    print(eval(c))

    print(complex_test_1(1, 2))
    print(complex_test_1(3))
    print(complex_test_2("1"))
    print(complex_test_2("1+2j"))
