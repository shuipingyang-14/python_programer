# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/22 11:42
@ file:     built-in_S.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


def set_test():
    """
    创建一个无序不重复元素集合
    :return:
    """
    x = set('hello')
    y = set('world')
    print(x, y)  # {'e', 'l', 'h', 'o'} {'o', 'r', 'l', 'w', 'd'} 重复元素的被删除

    print(x & y)  # 交集 {'o', 'l'}
    print(x | y)  # 并集 {'r', 'h', 'd', 'e', 'o', 'w', 'l'}
    print(x - y)  # x的差集 {'e', 'h'}
    print(y - x)  # y的差集 {'d', 'r', 'w'}


def setattr_test():
    """
    设置属性值，该属性不一定是存在的
    :return:
    """

    class A(object):
        bar = 1

    a = A()
    print(getattr(a, 'bar'))  # 1 获取属性值

    setattr(a, 'bar', 5)  # 设置属性 bar 值
    print(getattr(a, 'bar'))  # 5 获取属性值
    print(a.bar)  # 5

    # 属性不存在
    class A():
        name = "runoob"

    a = A()
    setattr(a, "age", 28)
    print(a.age)  # 28


def slice_test():
    """
    切片对象
    :return:
    """
    myslice = slice(5)  # 设置截取5个元素的切片
    print(myslice)  # slice(None, 5, None)

    arr = list(range(10))
    print(arr)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(arr[myslice])  # [0, 1, 2, 3, 4]

    myslice = slice(3, 10, 2)  # 截取从3到10间隔一个元素
    print(myslice)  # slice(3, 10, 2)

    arr = list(range(1, 11))
    print(arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(arr[myslice])  # [4, 6, 8, 10]


def sorted_test():
    """
    对可迭代对象进行排序
    :return: 重新排序的列表
    """
    l = [1, 4, 3, 5, 8, 7]
    print(sorted(l))  # [1, 3, 4, 5, 7, 8]

    s = "hello world"
    s1 = sorted(s)
    print(s1)  # [' ', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w'] # 升序排列
    print("".join(s1))  # dehllloorw
    s2 = sorted(s, reverse=True)
    print(s2)  # ['w', 'r', 'o', 'o', 'l', 'l', 'l', 'h', 'e', 'd', ' '] 降序排列

    # 对字典进行排序
    d = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
    print(sorted(d))  # [1, 2, 3, 4, 5]

    # 利用key进行排序
    example_list = [5, 0, 6, 1, 2, 7, 3, 4]
    result_list = sorted(example_list, key=lambda x: x * -1)
    print(result_list)  # [7, 6, 5, 4, 3, 2, 1, 0]

    # 反向排序
    example_list = [5, 0, 6, 1, 2, 7, 3, 4]
    print(sorted(example_list, reverse=True))  # [7, 6, 5, 4, 3, 2, 1, 0]

    # 自定义key
    s = "This is a test string from Andrew"
    res = sorted(s.split(), key=str.lower)
    print(res)  # ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']

    # 对复杂对象的比较通常是使用对象的切片作为关键字
    student_tuples = [('bohn', 'A', 15), ('jane', 'B', 12), ('have', 'B', 10)]
    res = sorted(student_tuples, key=lambda stu: stu[2])  # 以年龄升序排序
    print(res)  # [('have', 'B', 10), ('jane', 'B', 12), ('bohn', 'A', 15)]

    res = sorted(student_tuples, key=lambda stu: stu[0])  # 以姓名升序排序
    print(res)  # [('bohn', 'A', 15), ('have', 'B', 10), ('jane', 'B', 12)]

    # 类对象排序
    class Student:
        def __init__(self, name, grade, age):
            self.name = name
            self.grade = grade
            self.age = age

        def __repr__(self):
            return repr((self.name, self.grade, self.age))

    student_objects = [Student('john', 'A', 15), Student('jane', 'B', 12), Student('dave', 'B', 10), ]
    res = sorted(student_objects, key=lambda stu: stu.age)
    print(res)  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

    # operator模块
    from operator import itemgetter, attrgetter
    res = sorted(student_tuples, key=itemgetter(2))
    print(res)  # [('have', 'B', 10), ('jane', 'B', 12), ('bohn', 'A', 15)]

    res = sorted(student_objects, key=attrgetter('age'))
    print(res)  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

    # operator模块支持多级排序
    # 先按成绩排序，再按年龄排序
    res = sorted(student_tuples, key=itemgetter(1, 2))
    print(res)  # [('bohn', 'A', 15), ('have', 'B', 10), ('jane', 'B', 12)]

    res = sorted(student_objects, key=attrgetter('grade', 'age'))
    print(res)  # [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

    # 排序稳定，当有相同关键字是，原始排序保留
    data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]  # [('blue', 1), ('blue', 2), ('red', 1), ('red', 2)]
    res = sorted(data, key=itemgetter(0))
    print(res)  # [('blue', 1), ('blue', 2), ('red', 1), ('red', 2)]

    s = sorted(student_objects, key=attrgetter('age'))
    print(s)  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

    s = sorted(s, key=attrgetter('grade'), reverse=True)
    print(s)  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


def staticmethod_test():
    """
    返回函数的静态方法
    :return:
    """

    class C(object):
        # def __init__(self, name):
        #     self.name = name
        #     print(name)

        @staticmethod
        def f(name):
            print("hello %s" % name)

    C.f("111")  # 静态方法无需实例化
    cobj = C()
    cobj.f('111')  # 也可以实例化后调用


def str_test():
    """
    将一个对象转换为字符串
    :return:
    """
    s = 'hello'
    print(type(str(s)))
    print(str(s))

    list = [1, 2, 3]
    print(type(str(list)))
    print(str(list))

    tuple = (1, 2, 3)
    print(type(str(tuple)))
    print(str(tuple))

    dict = {'1': 1, '2': 2, '3': 3}
    print(type(str(dict)))
    print(str(dict))


def sum_test():
    """
    可迭代对象进行求和
    :return:
    """
    s = [1, 2, 3, 4, 5]
    print(sum(s))  # 15

    s = (1, 2, 3, 4, 5)
    print(sum(s))  # 15

    print(sum((2, 3, 4), 1))  # 元组计算总和后再加 1   , 结果10

    print(sum([0, 1, 2, 3, 4], 2))  # 列表计算总和后再加 2  ，结果12


def super_test():
    """
    调用父类的方法
    :return:
    """
    class A:
        def add(self, x):
            y = x+1
            print(y)

    class B(A):
        def add(self, x):
            y = x+1
            super().add(x)
    b = B()
    b.add(2) # 3

class FooParent(object):
    def __init__(self):
        self.parent = "I'm the parent"
        print('------parent-----')

    def bar(self, message):
        print ("%s from Parent" % message)

class FooChlid(FooParent):
    def __init__(self):
        super().__init__()
        print('-----child----')

    def bar(self, message):
        super().bar(message)
        print('Child bar fuction')
        print(self.parent)

class A():
    def __init__(self):
        print('enter A')
        print('leave A')


class B(A):
    def __init__(self):
        print('enter B')
        super().__init__()
        print('leave B')


class C(A):
    def __init__(self):
        print('enter C')
        super().__init__()
        print('leave C')


class D(B, C):
    def __init__(self):
        print('enter D')
        super().__init__()
        print('leave D')

if __name__ == '__main__':
    set_test()
    setattr_test()
    slice_test()
    sorted_test()
    staticmethod_test()
    str_test()
    sum_test()
    super_test()
    fooChild = FooChlid()
    fooChild.bar('HelloWorld')
    # ------parent-----
    # -----child----
    # HelloWorld from Parent
    # Child bar fuction
    # I'm the parent
    D()
    # enter D
    # enter B
    # enter C
    # enter A
    # leave A
    # leave C
    # leave B
    # leave D