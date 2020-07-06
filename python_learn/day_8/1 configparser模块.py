# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/2 16:04
@ file:     1 confparser模块.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# 生成配置文件
import configparser

conf = configparser.ConfigParser()
conf['DEFAULT'] = {
    'ServerAliveInterval':'45',
    'Compression':'yes',
    'CompressionLevel':'9',
    'ForwordXll':'yes',
    'User':'xy'
}

conf['bitbucket.org'] = {'User':'hg'}
conf['topsecret.server.com'] = {'Host Port':'50022', 'ForwardXll':'no'}

with open('conf.ini', 'w') as conf_file:
    conf.write(conf_file)

"""
[DEFAULT]
serveraliveinterval = 45
compression = yes
compressionlevel = 9
forwordxll = yes
user = xy

[bitbucket.org]
user = hg

[topsecret.server.com]
host port = 50022
forwardxll = no

"""

# 查找文件
conf1 = configparser.ConfigParser()
print(conf1.sections())   # []
conf1.read('conf.ini')
print(conf1.sections())  # ['bitbucket.org', 'topsercet.server.com']
print('bytebong.com' in conf1)  # False
print('bitbucket.org' in conf1)  # True

print(conf1['bitbucket.org']['User'])  # hg
print(conf1['DEFAULT']['Compression'])  # yes
print(conf1['topsecret.server.com']['ForwardXll'])  # no

print(conf1['bitbucket.org'])   # <Section: bitbucket.org>

for key in conf1['bitbucket.org']:     # 注意,有default会默认default的键
    print(key)  # user serveraliveinterval compression compressionlevel forwordxll
#
print(conf1.options('bitbucket.org'))  # 同for循环,找到'bitbucket.org'下所有键
# ['user', 'serveraliveinterval', 'compression', 'compressionlevel', 'forwordxll']

print(conf1.items('bitbucket.org'))    #找到'bitbucket.org'下所有键值对
# [('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwordxll', 'yes'), ('user', 'hg')]

print(conf1.get('bitbucket.org','compression')) # yes       get方法Section下的key对应的valuevvvv


# 增删改操作
conf2 = configparser.ConfigParser()
conf2.read('conf.ini')
conf2.add_section('ysp')

conf2.remove_section('bitbucket.org')
conf2.remove_option('topsecret.server.com',"forwardx11")

conf2.set('topsecret.server.com','k1','11111')
conf2.set('ysp', 'k2', '22222')
conf2.write(open('new.ini', 'w'))