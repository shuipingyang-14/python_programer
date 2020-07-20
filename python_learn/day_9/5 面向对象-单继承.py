# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/20 14:30
@ file:     5 面向对象-单继承.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# 一个类别A“继承自”另一个类别B，就把这个A称为“B的子类别”，而把B称为“A的父类别”也可以称“B是A的超类”
# 继承使得子类别具有父类别的各种属性和方法，不需要编写相同代码
# 在令子类别继承父类别同时，可以重新定义某些属性，并重写某些方法，覆盖父类别的原有属性和方法，使其获得与父类别不同功能

class Person:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

class Dog:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

# 继承
class Animal(object):
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

class Person(Animal):
    pass

class Cat(Animal):
    pass

class Dog(Animal):
    pass

# 继承的优点
# a. 增加类的耦合性
# b. 减少重复性代码
# c. 使得代码更加规范化，合理化

# 继承分类：单继承，多继承
# Animal：父类，基类，超累
# Person,Cat,Dog：子类，派生类

# 单继承
class Animal(object):
    type_name = '动物类'

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def eat(self):
        print(self)
        print('吃东西')

class Person(Animal):
    pass

class Cat(Animal):
    pass

class Dog(Animal):
    pass


# 类名
print(Person.type_name)   # 动物类
Person.eat(111)    # 111  吃东西
print(Person.type_name)   # 动物类

# 对象
# 实例化对象
p1 = Person('jason', '男', 18)
print(p1.__dict__)   # {'name': 'jason', 'sex': '男', 'age': 18}

# 对象执行类的父类的属性，方法
print(p1.type_name)  # 动物类
p1.type_name = '6666'
print(p1)  # <__main__.Person object at 0x000001E7F0ABA2E0>
p1.eat()   # <__main__.Person object at 0x000001E7F0ABA2E0>   吃东西
print(p1.type_name)  # 6666
print(p1.__dict__)   # {'name': 'jason', 'sex': '男', 'age': 18, 'type_name': '6666'}

class Person(Animal):

    def eat(self):
        print('%s 吃饭' % self.name)

p1 = Person('barry','男',18)
# 实例化对象时必须执行__init__方法,类中没有，从父类找，父类没有，从object类中找
p1.eat()  # barry 吃饭
# 先要执行自己类中的eat方法，自己类没有才能执行父类中的方法

# 同时执行类及父类方法
# 方法一：如果想执行父类的func方法，这个方法并且子类中夜用，那么就在子类的方法中写上：父类.func(对象,其他参数)
class Person(Animal):
    def __init__(self,name,sex,age,mind):
        '''
        self = p1
        name = '春哥'
        sex = 'laddboy'
        age = 18
        mind = '有思想'
        '''
        Animal.__init__(self,name,sex,age)  # 方法一
        self.mind = mind

    def eat(self):
        super().eat()
        print('%s 吃饭'%self.name)

p1 = Person('春哥','laddboy',18,'有思想')
print(p1.__dict__)  # {'name': '春哥', 'sex': 'laddboy', 'age': 18, 'mind': '有思想'}

# 方法二：super.func(参数)
class Person(Animal):
    def __init__(self,name,sex,age,mind):
        '''
        self = p1
        name = '春哥'
        sex = 'laddboy'
        age = 18
        mind = '有思想'
        '''
        super().__init__(name,sex,age)  # 方法一
        self.mind = mind

    def eat(self):
        super().eat()
        print('%s 吃饭'%self.name)


p1 = Person('春哥','laddboy',18,'有思想')
print(p1.__dict__)  # {'name': '春哥', 'sex': 'laddboy', 'age': 18, 'mind': '有思想'}

