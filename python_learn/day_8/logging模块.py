# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/2 16:37
@ file:     logging模块.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""
# 默认情况下Python的logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志
# 默认的日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG）
# 默认的日志格式为日志级别：Logger名称：用户输出消息


import logging
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

"""
结果：
WARNING:root:warning message
ERROR:root:error message
CRITICAL:root:critical message
"""

# 配置日志级别，日志格式，输出位置
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
#                     # datefmt='%Y/%m/%d-%H:%M:%S',
#                     filename='test.log',
#                     filemode='w')
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

# 参数说明
"""
filename：用指定的文件名创建FileHalder，日志存储在指定文件中
filemode：文件打开方式，制定了filename时使用此参数，默认值为'a'
format：指定handler使用的日志显示格式
datefmt：指定日期时间格式
level：设置rootlogger的日志级别
stream：用指定的stream创建StreamHandler，可指定输出到sys.stderr, sys.stdout或者文件f=open(‘test.log’,’w’))，默认为sys.stderr
同时列出了filename和stream两个参数，则stream参数会被忽略

format参数中可能用到的格式化串：
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s用户输出的消息
"""

# logger对象配置
logger = logging.getLogger()
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log', encoding='utf-8')

# 创建一个handler，输出到控制台
ch = logging.StreamHandler()


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setLevel(logging.ERROR)
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh) #logger对象可以添加多个fh和ch对象
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)

logger.debug('logger debug message\n')
logger.info('logger info message\n')
logger.warning('logger warning message\n')
logger.error('logger error message\n')
logger.critical('logger critical message\n')


# logging库提供了多个组件：Logger、Handler、Filter、Formatter
# Logger对象提供应用程序可直接使用的接口，Handler发送日志到适当的目的地，Filter提供了过滤日志信息的方法，Formatter指定日志显示格式
# 另外，可以通过：logger.setLevel(logging.Debug)设置级别,当然，也可以通过fh.setLevel(logging.Debug)单对文件流设置某个级别

