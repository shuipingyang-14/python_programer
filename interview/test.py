# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/13 11:15
@ file:     test.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


# class Book(object):
#     def __new__(cls, title):
#         print('this is __new__')
#         return super(Book, cls).__new__(cls)
#
#     def __init__(self, title):
#         print('this is __init__')
#         super(Book, self).__init__()
#         self.title = title
#
# b = Book('this python book...')
# print(b.title)

class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

