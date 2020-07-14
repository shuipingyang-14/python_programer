* 相同点
二者就是python面向对象语言中的函数，__new__比较少用，__init__使用的较多

* 不同点
1. __init__是当实例对象创建完成后被调用的，设置对象属性的一些初始值，通常用在初始化一个类实例的时候，是一个实例方法
2. __new__诗在实例创建之前调用，因为它的任务是创建实例然后返回实例对象，是一个静态方法
3. __new__现被调用，__init__后被调用，__new__的返回值（实例）将传递给__init__方法的第一个参数，然后__init__给这个实例设置参数

```python
class Book(object):
    def __new__(cls, title):
        print('this is __new__')
        return super(Book, cls).__new__(cls)

    def __init__(self, title):
        print('this is __init__')
        super(Book, self).__init__()
        self.title = title

b = Book('this python book...')
print(b.title)


# 结果：
# this is __new__
# this is __init__
# this python book... 
```

* 特别说明
1. 继承object的新式类才有__new__
2. __new__至少有一个参数cls，代表当前类，此参数实例化时由python解释器自动识别
3. __new__必须要有返回值，返回实例化出来的实例，可以return父类（通过super(当前类名, cls)）__new__出来的实例，或者直接是object的__new__出来的实例
4. __init__有一个参数self是__new__返回的实例，__init__在__new__的基础上可以完成一些其他初始化的动作，__init__不需要返回值
5. 如果__new__创建的是当前类的实例，会自动调用__init__函数，通过return语句里面调用的__new__函数的第一个参数cls保证是当前类实例，如果是其他类的类名，实际创建返回的就是其他类的实例，其实不会调用当前类的__init__函数，也不会调用其他类的__init__函数
6. 在定义子类时没有重新定义__new__()时，python默认调用该类的直接父类的__new__()方法来构造该类的实例，如果该类的父类也没有重写__new__()，见过一直按此规律追溯到object的__new__()方法，因为object是所有新式类的基类
7. 如果子类重写了__new__()方法，可以自由选择任意一个的其他新式类（必须是新式类，只有新式类必定有__new__()，所有新式类是object后代，经典类中没有__new__()方法)的__new__()方法创造实例，包括新式类的所有前代类和后代类，只要不构成递归死循环
8. 对于子类的__init__，调用规则和__new__一致，如果子类和父类的__init__函数都想调用，可以在子类的__init__函数中加入对父类__init__函数的调用
9. 尽量使用__init__函数，不要去自定义__new__函数，因为这两者在继承派生时的特性还是很不一样的
10. 将类比作制造商，__new__方法就是前期的原材料购买环节，__init__方法就是在有原材料的基础上，加工，初始化商品环节

* __init__方法
```python
class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
```
* __new__方法
__new__方法和__init__的参数一样，__init__在类实例创建后调用，__new__是创建类实例的方法
```python
class Person(object):
    def __new__(cls, name, age):
        print('this is __new__')
        return super(Person, cls).__new__(cls)

    def __init__(self, name, age):
        print('this is the __init__')
        self.name = name
        self.age = age

    def __str__(self):
        return '<Person: %s(%s)>' %(self.name, self.age)

if __name__ == '__main__':
    p = Person('zhangsan', 18)
    print(p)
    
# 结果
# this is __new__
# this is the __init__
# <Person: zhangsan(18)>

# 执行逻辑：
"""
1. p = Person(name, age)
2. 首先执行使用name和age参数来执行Person类的__new__方法，这个__new__方法会返回Person类的一个实例（通常情况下是使用 super(Persion, cls).__new__(cls) 这样的方式）
3. 然后利用这个实例来调用类的__init__方法，上一步里面__new__产生的实例也就是 __init__里面的的 self
"""
```

* __init__和__new__主要的区别：
1. __init__通常用于初始化一个新实例，控制初始化的过程，比如添加一些属性，做一些额外操作，发生在类实例被创建完成后，是实例级别的方法
2. __new__通常用于控制生成一个新实例过程，是类级别的方法

* __new__作用：
__new__是当继承一些不可变的class时(比如int,str,tuple)，提供一个自定义类实例化过程的途径，实现自定义的metaclass
```python
class PositiveInterger(int):
    def __new__(cls, value):
        return super(PositiveInterger, cls).__new__(cls, abs(value))
        
i = PositiveInterger(-3)
print(i)
```