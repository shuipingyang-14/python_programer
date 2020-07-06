# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/2 18:08
@ file:     logging配置.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

import os
import logging.config

# 定义日志输出格式
standard_format = '[%(asctime)s] [%(threadName)s:%(thread)d] [task_id:%(name)s] [%(filename)s:%(lineno)d]' \
                  '[%(levelname)s] [%(message)s]' #其中name为getlogger指定的名字
simple_format = '[%(levelname)s] [%(asctime)s] [%(filename)s:%(lineno)d] %(message)s'
id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式
logfile_dir = os.path.dirname(os.path.realpath(__file__))  # log文件目录
logfile_name = 'all.log'  # log文件名

# 如果不存在定义的目录，创建目录
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)

# log文件全路径
logfile_path = os.path.join(logfile_dir, logfile_name)

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}

def load_my_logging_cfg():
    logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
    logger = logging.getLogger(__name__)  # 生成一个log实例
    logger.info('It works!')  # 记录该文件的运行状态
    logger.debug('logger debug message')
    logger.info('logger info message')
    logger.warning('logger warning message')
    logger.error('logger error message')
    logger.critical('logger critical message')

if __name__ == '__main__':
    load_my_logging_cfg()