# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/9 16:44
@ file:     2 面向对象-对象.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


# 对象是从类中出来，只是类名加上()，这是一个实例化过程，会实例化一个对象

class Human:
    mind = '有思想'

    def __init__(self):
        print('666')
        print(self)

    def work(self):
        print('人类会工作')

    def tools(self):
        print('人类会使用工具')


obj = Human()  # 实例化对象，自动执行__init__方法
# 666
# <__main__.Human object at 0x000002B8105C1A90>
print(obj)
# <__main__.Human object at 0x000002B8105C1A90>

# 实例化对象发生的事:
"""
1. 在内存中开辟了一个对象空间
2. 自动执行类中的__init__方法，并将这个对象空间（内存地址）传给了__init__方法的第一个位置参数self
3. 在__init__ 方法中通过self给对象空间添加属性
"""


class Human:
    mind = '有思想'
    language = '使用语言'

    def __init__(self, name, sex, age, hobby):
        # self 和 obj 指向的是同一个内存地址同一个空间，下面就是通过self给这个对象空间封装四个属性。
        self.n = name
        self.s = sex
        self.a = age
        self.h = hobby
        print(self.n, self.s, self.a, self.h)  # barry 男 18 运动

    def work(self):
        print(self)
        print('人类会工作')

    def tools(self):
        print('人类会使用工具')


obj = Human('barry', '男', 18, '运动')

# 1. 对象操作对象空间属性
# a. 对象查询对象中所有属性
print(obj.__dict__)
# {'n': 'barry', 's': '男', 'a': 18, 'h': '运动'}

# b. 对象曹祖对象中单个属性
obj.job = 'IT'  # 增
del obj.n  # 删
obj.s = '女'  # 改
print(obj.s)  # 查
# 女
print(obj.__dict__)
# {'s': '女', 'a': 18, 'h': '运动', 'job': 'IT'}

# 2. 对象查看类中的属性
obj = Human('barry', '男', 18, '运动')
print(obj.mind)
# 有思想
print(obj.language)
# 使用语言
obj.a = 666
print(obj.a)
# 666

# 对象操作类中的方法
obj = Human('barry', '男', 18, '运动')
# barry 男 18 运动
# <__main__.Human object at 0x00000111BB80A7C0>
obj.work()
# 人类会工作
obj.tools()
# 人类会使用工具

# 类中的方法一般都是通过对象执行的（出去类方法，静态方法外），并且对象执行这些方法都会自动将对象空间传给方法中的第一个参数self.
# self其实就是类中方法（函数）的第一个位置参数，只不过解释器会自动将调用这个函数的对象传给self。所以咱们把类中的方法的第一个参数约定俗成设置成self, 代表这个就是对象
# 一个类可以实例化多个对象
#
obj1 = Human('小胖', '男', 20, '美女')
obj2 = Human('相爷', '男', 18, '肥女')
print(obj1, obj2)
# 小胖 男 20 美女
# 相爷 男 18 肥女
# <__main__.Human object at 0x00000224C74DA2E0> <__main__.Human object at 0x00000224C74A1A90>

print(obj1.__dict__)
# {'n': '小胖', 's': '男', 'a': 20, 'h': '美女'}
print(obj2.__dict__)
# {'n': '相爷', 's': '男', 'a': 18, 'h': '肥女'}
