# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/3 14:00
@ file:     3 time模块.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""
import time

time.sleep(0.5)  # (线程)推迟指定时间运行，单位为秒
time.time()  # 获取当前时间戳

# 表示时间的三种方式
# a. 时间戳(timestamp)：时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量
# 运行“type(time.time())”，返回的是float类型
print(time.time())  # 1593756663.4397957

# b. 格式化时间字符串(Format String)：'1999-12-06'
"""
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身"""
print(time.strftime("%Y-%m-%d %X"))
# 2020-07-03 14:12:08
print(time.strftime("%Y-%m-%d %H-%M-%S"))
# 2020-07-03 14-12-08

# c. 元组(struct_time)：struct_time元组共有9个元素共九个元素:(年，月，日，时，分，秒，一年中第几周，一年中第几天等）
"""
索引（Index）	属性（Attribute）	    值（Values）
0	            tm_year（年）	        比如2011
1	            tm_mon（月）	            1 - 12
2	            tm_mday（日）	        1 - 31
3	            tm_hour（时）	        0 - 23
4	            tm_min（分）	            0 - 59
5	            tm_sec（秒）	            0 - 60
6	            tm_wday（weekday）	    0 - 6（0表示周一）
7	            tm_yday（一年中的第几天）	1 - 366
8	            tm_isdst（是否是夏令时）	默认为0
"""
print(time.localtime()) # localtime将一个时间戳转换为当前时区的struct_time
# time.struct_time(tm_year=2020, tm_mon=7, tm_mday=3, tm_hour=14, tm_min=12, tm_sec=53, tm_wday=4, tm_yday=185, tm_isdst=0)

# 格式化时间->结构化时间
ft = time.strftime('%Y/%m/%d %H:%M:%S')
print(ft)  # 2020/07/03 14:19:53
st = time.strptime(ft,'%Y/%m/%d %H:%M:%S')
print(st) # time.struct_time(tm_year=2020, tm_mon=7, tm_mday=3, tm_hour=14, tm_min=19, tm_sec=53, tm_wday=4, tm_yday=185, tm_isdst=-1)

# 结构化时间->时间戳
t = time.mktime(st)
print(t)  # 1593757289.0

# 结构化时间->格式化时间
ft = time.strftime('%Y/%m/%d %H:%M:%S',st)
print(ft)  # 2020/07/03 14:21:59

# 时间戳->结构化时间
t = time.time()
st = time.localtime(t)
print(st)  # time.struct_time(tm_year=2020, tm_mon=7, tm_mday=3, tm_hour=14, tm_min=22, tm_sec=38, tm_wday=4, tm_yday=185, tm_isdst=0)

#结构化时间 --> %a %b %d %H:%M:%S %Y串
print(time.asctime(time.localtime(1500000000)))  # Fri Jul 14 10:40:00 2017
print(time.asctime())  # Fri Jul  3 14:54:35 2020

#test1: 不加参数，默认就是time.localtime()返回的时间结构元组
print("test1: print time.asctime():",time.asctime())
# Fri Jul  3 14:47:07 2020

#test2: time.loaltime() 本地时间
t1 = time.localtime()
print("test2: t1(localtime):",t1)

# time.struct_time(tm_year=2020, tm_mon=7, tm_mday=3, tm_hour=14, tm_min=47, tm_sec=7, tm_wday=4, tm_yday=185, tm_isdst=0)
print("test2: time.asctime(t1):",time.asctime(t1))
# Fri Jul  3 14:47:07 2020

#test3: time.gmtime() 格林威治标准时间
t2 = time.gmtime()
print("test3: t2(gmtime):",t2)
# time.struct_time(tm_year=2020, tm_mon=7, tm_mday=3, tm_hour=6, tm_min=47, tm_sec=7, tm_wday=4, tm_yday=185, tm_isdst=0)
print("test3: time.asctime(t2):",time.asctime(t2))
# Fri Jul  3 06:47:07 2020

#test4: 按time_struct,人工指定时间结构元组
t3 = (2018,5,27,1,5,27,6,147,-1)
print("test4: t3:",t3)
print("test4: time.asctime(t3):",time.asctime(t3))
# Sun May 27 01:05:27 2018

# 时间戳 --> %a %d %d %H:%M:%S %Y串
# time.ctime(时间戳)  如果不传参数，直接返回当前时间的格式化串
print(time.ctime())
# Fri Jul  3 14:55:50 2020
print(time.ctime(1500000000))
# Fri Jul 14 10:40:00 2017

t = time.time()
ft = time.ctime(t)
print(ft)  # Fri Jul  3 14:55:50 2020

st = time.localtime()
ft = time.asctime(st)
print(ft)  # Fri Jul  3 14:55:50 2020


# 计算时间戳
true_time = time.mktime(time.strptime('1997-04-29 00:00:00','%Y-%m-%d %H:%M:%S'))
print(true_time)
time_now=time.time()

dif_time = time_now - true_time
struct_time = time.gmtime(dif_time)
print('过去了%d年%d月%d天%d小时%d分钟%d秒'%(struct_time.tm_year-1970,struct_time.tm_mon-1,
                                       struct_time.tm_mday-1,struct_time.tm_hour,
                                       struct_time.tm_min,struct_time.tm_sec))
# 过去了23年2月6天15小时0分钟9秒