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
在python中，内部含有'__Iter__'方法并且含有'__next__'方法的对象就是迭代器
"""
# 2.1 判断对象是不是迭代器
