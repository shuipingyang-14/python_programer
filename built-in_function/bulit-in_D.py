# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/1 18:49
@ file:     bulit-in_D.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

class Test():
    x = 10
    y = -5
    z = 0

def delattr_test():
    """
    删除属性测试
    :return:
    """
    point1 = Test()
    print('x = ', point1.x)
    print('y = ', point1.y)
    print('z = ', point1.z)

    delattr(Test, 'z')
    print('--删除 z 属性后--')
    print('x = ', point1.x)
    print('y = ', point1.y)

    # 触发错误
    # print('z = ', point1.z)   # AttributeError: 'Test' object has no attribute 'z'


def dict_test():
    """
    创建字典
    :return:
    """
    res1 = dict()  # 创建空字典
    print(res1)
    res2 = dict(a='a', b='b', t='t')  # 传入关键字
    print(res2)
    res3 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典
    print(res3)
    res4 = dict([('one', 1), ('two', 2), ('three', 3)])  # 可迭代对象方式创建字典
    print(res4)

def dir_test():
    """
    返回当前范围内的变量、方法和定义的类型列表
    :return:
    """
    print(dir(()))
    print(dir([]))
    print(dir({}))
    print(dir(""))

def divmod_test():
    """
    返回包含商和余数的元组
    :return:
    """
    print(divmod(7, 2))   # (3. 1)
    print(divmod(8, 2))   # (4. 0)
    print(divmod(7, -2))   # (-4. -1)
    print(divmod(-7, 2))   # (-4. 1)


if __name__ == '__main__':
    delattr_test()
    dict_test()
    dir_test()
    print(dir())
    divmod_test()
