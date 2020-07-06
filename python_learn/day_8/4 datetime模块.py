# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/3 15:00
@ file:     datetime模块.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

import datetime
now_time = datetime.datetime.now() # 当前时间
print(now_time) # 2020-07-03 15:02:14.630505
# 只能调整的字段：weeks days hours minutes seconds
print(datetime.datetime.now() + datetime.timedelta(weeks=3)) # 三周后
# 2020-07-24 15:02:14.630505
print(datetime.datetime.now() + datetime.timedelta(weeks=-3)) # 三周前
# 2020-06-12 15:02:14.630505
print(datetime.datetime.now() + datetime.timedelta(days=-3)) # 三天前
# 2020-06-30 15:02:14.630505
print(datetime.datetime.now() + datetime.timedelta(days=3)) # 三天后
# 2020-07-06 15:02:14.630505
print(datetime.datetime.now() + datetime.timedelta(hours=5)) # 5小时后
# 2020-07-03 20:02:14.630505
print(datetime.datetime.now() + datetime.timedelta(hours=-5)) # 5小时前
# 2020-07-03 10:02:14.630505
print(datetime.datetime.now() + datetime.timedelta(minutes=-15)) # 15分钟前
# 2020-07-03 14:47:14.630505
print(datetime.datetime.now() + datetime.timedelta(minutes=15)) # 15分钟后
# 2020-07-03 15:17:14.630505
print(datetime.datetime.now() + datetime.timedelta(seconds=-70)) # 70秒前
# 2020-07-03 15:01:04.630505
print(datetime.datetime.now() + datetime.timedelta(seconds=70)) # 70秒后
# 2020-07-03 15:03:24.630505

current_time = datetime.datetime.now()
print(current_time.replace(year=1970)) # 直接调整到1977年
# 1970-07-03 15:11:55.666357
print(current_time.replace(month=1))  # 直接调整到1月份
# 2020-01-03 15:11:55.666357
print(current_time.replace(year=1997, month=4, day=29))  # 1997-04-29
# 1997-04-29 15:11:55.666357
# 将时间戳转换成时间
print(datetime.date.fromtimestamp(1500000000))  # 2017-07-14