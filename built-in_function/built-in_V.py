# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/23 9:58
@ file:     built-in_V.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

def vars_test():
    """
    返回对象object的属性和属性值的字典对象，如果没有参数，就打印当前调用位置的属性和属性值 类似 locals()
    :return:
    """
    print(vars()) # {}

    class A:
        a = 1

    print(vars(A)) # {'__module__': '__main__', 'a': 1, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}

    a = A()
    print(vars(a)) # {}

if __name__ == '__main__':
    print(vars()) # {'__name__': '__main__', '__doc__': '\n@ author:   ysp\n@ time：    2020/6/23 9:58\n@ file:     built-in_V.py\n@ IDE:      PyCharm\n@ version:  python 3.8.3\n', '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000197A665A2E0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'E:/PyCode/python_programer/built-in_function/built-in_V.py', '__cached__': None, 'vars_test': <function vars_test at 0x00000197A65751F0>}
    vars_test()