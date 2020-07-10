# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/5 22:03
@ file:     5 datetime模块.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# date类
from datetime import date

d1 = date(2020, 5, 20)
print(d1)  # 2020-05-202
# 获取date类的各个属性
print(d1.year)  # 2020
print(d1.month)  # 5
print(d1.day)  # 20

# time类
from datetime import time

t1 = time(22, 6, 20)
print(t1)  # 22:06:20
# 获取time类的各个属性
print(t1.hour)  # 22
print(t1.minute)  # 6
print(t1.second)  # 20

# datetime类
from datetime import datetime

dt = datetime(2019, 11, 11, 11, 11, 11)
print(dt)  # 2019-11-11 11:11:11
# 获取datetime类的各个属性
print(dt.year)  # 2019
print(dt.month)  # 11
print(dt.day)  # 11
print(dt.hour)  # 11
print(dt.minute)  # 11
print(dt.second)  # 11

# datetime进行数学运算
from datetime import timedelta
# timedelta : 时间变化量

td = timedelta(days=1)
print(td)  # 1 day, 0:00:00

now_time = datetime.now()  # 现在的时间
# 只能调整的字段：weeks days hours minutes seconds
print(datetime.now() + timedelta(weeks=3)) # 三周后
# 2020-07-26 22:16:31.054370

# 2009-01-17
print(datetime.now() + timedelta(weeks=-3)) # 三周前
# 2020-06-14 22:16:31.054370

print(datetime.now() + timedelta(days=-3)) # 三天前
# 2020-07-02 22:16:31.054370

print(datetime.now() + timedelta(days=3)) # 三天后
# 2020-07-08 22:16:31.054370

print(datetime.now() + timedelta(hours=5)) # 5小时后
# 2020-07-06 03:16:31.054370

print(datetime.now() + timedelta(hours=-5)) # 5小时前
# 2020-07-05 17:16:31.054370

print(datetime.now() + timedelta(minutes=-15)) # 15分钟前
# 2020-07-05 22:01:31.054370

print(datetime.now() + timedelta(minutes=15)) # 15分钟后
# 2020-07-05 22:31:31.054370

print(datetime.now() + timedelta(seconds=-70)) # 70秒前
# 2020-07-05 22:15:21.054370

print(datetime.now() + timedelta(seconds=70)) # 70秒后

current_time = datetime.now()
# 2020-07-05 22:17:41.054370

# 可直接调整到指定的 年 月 日 时 分 秒 等

print(current_time.replace(year=1977))  # 直接调整到1977年
# 1977-07-05 22:16:31.054370
print(current_time.replace(month=1))  # 直接调整到1月份
# 2020-01-05 22:16:31.054370

print(current_time.replace(year=1989,month=4,day=25))  # 1989-04-25 18:49:05.898601
# 1989-04-25 22:16:31.054370

# 将时间戳转化成时间
print(date.fromtimestamp(1232132131))  # 2009-01-17
