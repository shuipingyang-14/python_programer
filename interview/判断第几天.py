# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/26 11:08
@ file:     判断第几天.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

import datetime

def day_of_year():
    year = int(input("请输入年份："))
    month = int(input("请输入月份："))
    day = int(input("请输入天："))
    date1 = datetime.date(year=year, month=month, day = day)
    date2 = datetime.date(year=year, month=1, day=1)
    return (date1-date2).days

if __name__ == '__main__':
    day = day_of_year()
    print(day)