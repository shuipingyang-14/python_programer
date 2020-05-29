# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/26 15:18
@ file:     迭代器.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# 1. 可迭代对象
"""
可迭代对象：在python中，但凡内部含有__iter__方法的对象，都是可迭代对象（str  list   tuple  dic  set  range 文件句柄等）
可迭代对象就是一个可以重复取值的实实在在的东西
可迭代对象可以通过判断该对象是否有’__iter__’方法来判断

可迭代对象的缺点：
1. 占用内存
2. 可迭代对象不能迭代取值（除去索引，key以外）
"""

# 1.1. 查看对象内部方法
s1 = 'alex'
print(dir(s1))  # dir()会返回一个列表，这个列表中含有该对象的以字符串的形式所有方法名

# 1.2. 判断对象是不是可迭代对象
s1 = 'alex'
i = 100
print('__iter__' in dir(s1))   # True
print('__iter__' in dir(i))    # False

# 2. 迭代器
"""
迭代器，是一个可以迭代取值的工具
迭代器，实现了无参数的__next__方法，返回序列中的下一个元素，如果没有元素了，那么抛出StopIteration异常.python中的迭代器还实现了__iter__方法，因此迭代器也可以迭代
在python中，内部含有'__iter__'方法并且含有'__next__'方法的对象就是迭代器
"""
# 2.1 判断对象是不是迭代器
s1 = 'alex'
t1 = (1,2,3)
l1 = [1,2,3]
set1 = {1,2,3}
d1 = {'a':1, 'b':2}
f = open('test.txt', encoding='utf-8', mode='w')
print("__iter__" in dir(s1))    # True
print("__iter__" in dir(t1))    # True
print("__iter__" in dir(l1))    # True
print("__iter__" in dir(set1))  # True
print("__iter__" in dir(d1))    # True
print("__iter__" in dir(f))    # True

print("__next__" in dir(s1))    # False
print("__next__" in dir(t1))    # False
print("__next__" in dir(l1))    # False
print("__next__" in dir(set1))  # False
print("__next__" in dir(d1))    # False
print("__next__" in dir(f))    # True

# 2.2 可迭代对象转换成迭代器
l1 = [1,2,3,4,5]
obj1 = l1.__iter__()
obj2 = iter(l1)
print("__next__" in dir(obj1))   # True
print("__next__" in dir(obj2))   # True

# 2.3 迭代取值
# 可迭代对象是不可以一直迭代取值的（除去用索引，切片以及Key），但是转化成迭代器就可以了，迭代器是利用__next__()进行取值：
l1 = [1,2,3]
obj = l1.__iter__()   # <list_iterator object at 0x0000021854671370>
print(obj)
ret = obj.__next__()   # 1
print(ret)
ret = obj.__next__()   # 2
print(ret)
ret = obj.__next__()  # 3
print(ret)

# 2.4 while模拟for循环
# for循环的内部机制是：将可迭代对象转换成迭代器，然后利用next进行取值，最后利用异常处理处理StopIteration抛出的异常
l1 = [1, 2, 3, 4, 5, 6]
# 1 将可迭代对象转化成迭代器
obj = iter(l1)
# 2,利用while循环，next进行取值
while 1:
    # 3,利用异常处理终止循环
    try:
        print(next(obj))
    except StopIteration:
        break

# 2.5 迭代器的优点：
# a. 节省内存
# b. 迭代器在内存中相当于只占一个数据的空间：因为每次取值都上一条数据会在内存释放，加载当前的此条数据
# c. 惰性机制, next一次，取一个值，绝不过多取值​

# 2.6 迭代器的缺点：
# a. 不能直观的查看里面的数据
# b. 取值时不走回头路，只能一直向下取值
l1 = [1, 2, 3, 4, 5, 6]
obj = iter(l1)

for i in range(2):
    print(next(obj))

for i in range(2):
    print(next(obj))

# 2.7 可迭代对象与迭代器对比
"""
可迭代对象：是一个私有的方法比较多，操作灵活（比如列表，字典的增删改查，字符串的常用操作方法等）,比较直观，但是占用内存，而且不能直接通过循环迭代取值的这么一个数据集
应用：当你侧重于对于数据可以灵活处理，并且内存空间足够，将数据集设置为可迭代对象是明确的选择

迭代器：是一个非常节省内存，可以记录取值位置，可以直接通过循环+next方法取值，但是不直观，操作方法比较单一的数据集
应用：当你的数据量过大，大到足以撑爆你的内存或者你以节省内存为首选因素时，将数据集设置为迭代器是一个不错的选择
"""