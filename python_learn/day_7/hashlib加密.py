# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/1 19:15
@ file:     hashlib加密.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# 1. hashlib提供常用的摘要算法，如md5，sha1等等
# 摘要算法：又称哈希算法，散列算法，通过一个函数，把任意长度数据转换为一个长度固定的数据串（16进制字符串表示）
# 摘要算法：通过摘要函数f()对任意长度数据data计算出固定长度的摘要digst，目的是为了发现原始数据是否被人篡改
# 摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data很困难，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同

# 2. 产生hash值的三个阶段
import hashlib
# a. 造出hash工厂
hash = hashlib.sha256('898oaFs09f'.encode('utf-8'))  # 同一种hash算法得到的长度是固定的
# b. 运送原材料
hash.update('alvin'.encode('utf8'))                     #工厂传入的原材料都是bytes类型
# c. 产出hash值
print(hash.hexdigest())  # e79e68f070cdedcfe63eaf1a2e92c83b4cfb1b5c6bc452d214c1b7e77cdfd1c7

md5 = hashlib.md5()   # 括号内也可以传值，类型也要求是bytes类型
md5.update('你好呀！'.encode('utf-8'))
print(md5.hexdigest())   # 9e49eb8e75b9a87424e388b862ea5f83

# 多次调用，与上述hash的结果一样
import hashlib
m=hashlib.md5('你'.encode('utf-8'))          # 括号内也可以传值，类型也要求是bytes类型
m.update('好呀！'.encode('utf-8'))
print(m.hexdigest()) # 9e49eb8e75b9a87424e388b862ea5f83

# 3. 校验文件的一致性（保证下载文件过程中不丢包，保证下载数据完整性）
m = hashlib.md5()
with open(r'E:\PyCode\python_programer\python_learn\day_7\test.json', 'rb') as f:
    for line in f:
        m.update(line)
print(m.hexdigest())   # 27f68dff5c9066ec83792aa0df8dd7e5

m = hashlib.md5()
with open(r'E:\PyCode\test.json', 'rb') as f:
    for line in f:
        m.update(line)
print(m.hexdigest())   # 27f68dff5c9066ec83792aa0df8dd7e5

# 4. 明文密码进行加密
# pwd = input("输入密码：").strip()     # 111
#
# m = hashlib.md5()
# m.update(pwd.encode('utf-8'))
# print(m.hexdigest())   # 698d51a19d8a121ce581499d7b701668

# 对密码进行加密，进一步加密
# pwd = input("输入密码：").strip()     # 111
#
# m = hashlib.md5()
# m.update('一行白鹭上青天'.encode('utf-8'))         #对密码加其他字符
# m.update(pwd.encode('utf-8'))
# print(m.hexdigest())   # 3019eb85b4dec892a25c214f769aca97

# 破解用户注册密码
pwd = {    # 可以通过random实现对pwd中的内容
    'alex3714',
    'alex1313',
    'alex94139413',
    'alex123456',
    '123456alex',
    'a123lex',
}


def make_passwd_dic(pwd):   # 通过明文密码列表，造出与之对应的hash值得字典
    dic = {}
    for index in pwd:
        m = hashlib.md5()     # 使用md5算法，造了一个工厂
        m.update(index.encode('utf-8'))   # 给工厂运送原材料(即我们要加密的内容)
        dic[index] = m.hexdigest()    # 产出hash值（即最终的产品），将其加入到我们事先造好的空字典中，字典形式:{密码：hash值}
    return dic


def break_code(cryptograph,passwd_dic):      #判断拦截的hash值是否与字典中事先造好的hash值相等，相等则说明成功进行破解
    for k,v in passwd_dic.items():
        if v == cryptograph:
            print('密码是===>%s' %k)

cryptograph='aee949757a2e698417463d47acac93df'     #我们拦截拿到的密码，经过加密的hash值
break_code(cryptograph,make_passwd_dic(pwd))   #将要破解的密码hash值，和事先造好的hash的字典当做函数的实参传给对应的形参

# sha加密
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())   # 2c76b57293ce30acef38d98f6046927161b46a44

# 打印进度条函数
import sys
import time

def progress(percent, width=50):
    if percent >= 1:
        percent = 1
    show_str = ('%%-%ss' %width) % (int(width*percent)*'|')
    print('\r%s %d%%' %(show_str, int(100*percent)), end='')

data_size = 1025
recv_size= 0

while recv_size < data_size:
    time.sleep(0.1)  # 模拟数据传输延迟
    recv_size += 10  # 每次收1024

    percent = recv_size / data_size  # 接受的比例
    progress(percent, width=70)  # 进度条宽度