# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/13 9:51
@ file:     3 面向对象-类空间.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


# 1. 添加对象属性:
# 对象的属性不仅可以在__init__里面添加，还可以在类的其他方法或者类的外面添加

class A:
    def __init__(self, name):
        self.name = name

    def func(self, sex):
        self.sex = sex


obj = A('barry')
obj.age = 19
print(obj.__dict__)  # {'name': 'barry', 'age': 19}

obj = A('alex')
obj.func('男')
print(obj.__dict__)  # {'name': 'alex', 'sex': '男'}

# 2. 添加类的静态属性：
# 类的属性不仅可以在类内部添加，也可以在类的外部添加

class B:
    def __init__(self, name):
        self.name = name

    def func(self, sex):
        self.sex = sex

    def func1(self):
        B.bbb = 'ccc'

B.aaa = 'aaa'
print(B.__dict__)
# {'__module__': '__main__', '__init__': <function B.__init__ at 0x0000025BACDF2430>, 'func': <function B.func at 0x0000025BACDF24C0>,
# 'func1': <function B.func1 at 0x0000025BACDF2550>, '__dict__': <attribute '__dict__' of 'B' objects>, '__weakref__': <attribute '__weakref__' of 'B' objects>,
# '__doc__': None, 'aaa': 'aaa'}

B.func1(111)
print(B.__dict__)
# {'__module__': '__main__', '__init__': <function B.__init__ at 0x0000025AF23623A0>, 'func': <function B.func at 0x0000025AF2362430>,
# 'func1': <function B.func1 at 0x0000025AF23624C0>, '__dict__': <attribute '__dict__' of 'B' objects>, '__weakref__': <attribute '__weakref__' of 'B' objects>,
# '__doc__': None, 'aaa': 'aaa', 'bbb': 'ccc'}

# 3. 对象找类属性：
# 对象可以找到类，是因为对象空间中有类对象指针
# 对象查找属性的顺序：先从对象空间找  ------> 类空间找 ------> 父类空间找 ------->.....
# 类名查找属性的顺序：先从本类空间找 -------> 父类空间找--------> ........
# 上面的顺序都是单向不可逆，类名不可能找到对象的属性

