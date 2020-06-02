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

if __name__ == '__main__':
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