# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/25 18:45
@ file:     1 function.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

def add(a, b):
    """
    对两个数求和
    :param a: 数值1
    :param b: 数值2
    :return: 数值1+数值2
    """
    c = a+b
    return c

def max(a, b):
    """
    求两个数之间的最大值
    :param a: 数值1
    :param b: 数值2
    :return: 两个数之间较大的数
    """
    # if a > b:
    #     return a
    # else:
    #     return b
    c = a if a > b else b
    return c

def date(sex, age, hobby):
    print('性别: %s，年龄：%s,爱好：%s' %(sex, age, hobby))

def stu_info(name, age=18, sex='男'):
    print("录入学生信息")
    print(name, age, sex)
    print("录入完毕")

if __name__ == '__main__':
    res = add(4,5)
    print(res)
    res = max(-1, 3)
    print(res)
    # 关键字参数
    date(hobby='唱歌', sex='女', age='25~30')
    # 混合参数
    date('男', hobby='跳舞', age='25~30')
    # 位置参数 ： 位置参数其实与实参角度的位置参数是一样的，就是按照位置从左至右，一一对应
    date('女', '25-30', '读书')
    # 默认值参数
    stu_info('张三', 20, '男')
    stu_info('里斯', 19)
    stu_info('张三')