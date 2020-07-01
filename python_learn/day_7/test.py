# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/1 11:03
@ file:     test.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

db_type = input(">>: ")
if db_type == 'mysql':
    import mysql as db
elif db_type == 'postgres':
    import postgres as db

db.sqlparse()
