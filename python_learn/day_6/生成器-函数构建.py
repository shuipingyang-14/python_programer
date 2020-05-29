# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/27 18:16
@ file:     生成器-函数构建.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# 生成器
"""
生成器本质是迭代器
迭代器都是Python给你提供的已经写好的工具或者通过数据转化得来的，（比如文件句柄，iter([1,2,3])
生成器是用python代码构建的工具
"""


# 通过生成器函数构建生成器
def fun():
    print(11)
    return 22


ret = fun()
print(ret)  # 11    22


def fun():
    print(11)
    yield 22  # 函数中存在yield,那么这个函数就是一个生成器函数.


ret = fun()  # 这个时候函数不会执⾏. ⽽是获取到⽣成器
print(ret)  # <generator object fun at 0x000001BC4D836B30>
result = ret.__next__()
print(result)  # 11    22


# 生成器函数写多个yield
def func():
    print(111)
    yield 222
    print(333)
    yield 444


gener = func()
ret1 = gener.__next__()
print(ret1)  # 111    222
ret2 = gener.__next__()
print(ret2)  # 333   444
# ret3 = gener.__next__()
# print(ret3)    # StopIteration
# 当程序运行完最后一个yield,那么后面继续运行next()程序会报错，一个yield对应一个next，next超过yield数量，就会报错，与迭代器一样

# yield 和 return 的区别
"""
return 一般在函数中只设置一个，作用是终止函数，并且给函数的执行者返回值
yield 在生成器函数中可设置多个，不会终止函数，next会获取对应yield生成的元素
"""


# 应用
# 老男孩向楼下卖包子的老板订购了10000个包子.包子铺老板非常实在，一下就全部都做出来
# 直接把包子全部做出来，占用内存
def eat():
    lst = []
    for i in range(1, 10000):
        lst.append('包子' + str(i))
    return lst


e = eat()
print(e)


# 吃一个生产一个，非常的节省内存，而且还可以保留上次的位置
def eat():
    for i in range(1, 10000):
        yield '包子' + str(i)


e = eat()
for i in range(20):
    print(next(e))
# 多次next包子的号码是按照顺序记录的
for i in range(10):
    print(next(e))


# send方法
# next只能获取yield生成的值，但是不能传递至
def gen(name):
    print(f"{name} ready to eat")
    while 1:
        food = yield
        print(f"{name} start to eat {food}")


dog = gen('aaa')
next(dog)
next(dog)
next(dog)

# 使用send方法
dog = gen('alex')
next(dog)  # 第一次必须用next让指针停留在第一个yield后面
# 与next一样，可以获取到yield的值
ret = dog.send('骨头')


dog = gen('alex')
next(dog)
# 还可以给上一个yield发送值
dog.send('骨头')
dog.send('狗粮')
dog.send('香肠')

# send和next区别
"""
相同点：send和next都可以让生成器对应的yield向下执行一次，都可以获取到yield生成的值
不同点：第一次获取yield值只能用next不能用send(可以用send(None))，send可以给上一个yield传递值
"""

# yield from
def func():
    lst = ['卫龙','老冰棍','北冰洋','牛羊配']
    yield lst
g = func()
print(g)   # <generator object func at 0x00000246F3AFE970>
print(next(g))  # 只是返回一个列表

def func():
    lst = ['卫龙','老冰棍','北冰洋','牛羊配']
    yield from lst
g = func()
print(g)  # <generator object func at 0x00000246F3AFE9E0>
# 将这个可迭代对象(列表)的每个元素当成迭代器的每个结果进行返回
print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''
yield from ['卫龙','老冰棍','北冰洋','牛羊配']
等同于：
    yield '卫龙'
    yield '老冰棍'
    yield '北冰洋'
    yield '牛羊配'
'''

# yield from 是将列表中的每一个元素返回,所以 如果写两个yield from 并不会产生交替的效果
def func():
    l1 = ['卫龙','老冰棍','北冰洋','牛羊配']
    l2 = ['馒头', '花卷', '大饼']
    yield from l1
    yield from l2

gen = func()
for i in gen:
    print(i)
