# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/1 18:57
@ file:     pickle序列化模块.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# pickle模块：将python所有数据结构及对象转换成bytes类型，然后反序列还原
# 用于网络传输：dumps，loads
import pickle

dic = {'k1': '测试1', 'k2': '测试2', 'k3': '测试3'}
str_dic = pickle.dumps(dic)
print(type(str_dic), str_dic)  # bytes类型

dic2 = pickle.loads(str_dic)
print(type(dic2), dic2)  # 字典 <class 'dict'> {'k1': '测试1', 'k2': '测试2', 'k3': '测试3'}


# 序列化对象
def func():
    print(666)


ret = pickle.dumps(func)
print(type(ret), ret)

f1 = pickle.loads(ret)  # # f1得到 func函数的内存地址
f1()  # 执行func函数

# 用于文件读写：dump，load
import pickle
dic = {(1, 2): 'oldboy', 1: True, 'set': {1, 2, 3}}
print(dic)
f = open('pick序列化', mode='wb')
res = pickle.dump(dic, f)
print(type(res), res)
f.close()
with open('pick序列化', mode='rb') as f1:
    res = pickle.load(f1)
    print(type(res), res)  # <class 'dict'> {(1, 2): 'oldboy', 1: True, 'set': {1, 2, 3}}

# pickle序列化存储多个数据到一个文件中
import pickle
dic1 = {'name':'oldboy1'}
dic2 = {'name':'oldboy2'}
dic3 = {'name':'oldboy3'}

f = open('pick多数据',mode='wb')
pickle.dump(dic1, f)
pickle.dump(dic2, f)
pickle.dump(dic3, f)
f.close()

f = open('pick多数据', mode='rb')
while True:
    try:
        print(pickle.load(f))
    except EOFError:
        break

f.close()


