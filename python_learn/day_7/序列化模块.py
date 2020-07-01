# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/1 11:36
@ file:     序列化模块.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# 序列化：将一种数据结构（如字典，列表）等转换成一个特殊的序列（字符串护着bytes）的过程叫做序列化

# json序列化可以解决写入文件的问题，也可解决网络传输问题

# 序列化模块就是将一个常见的数据结构转化成一个特殊的序列，并且这个特殊的序列还可以反解回去
# 主要用途：文件读写数据，网络传输数据

# 1. 序列化模块：
# a. json模块：不同语言都遵循的数据转化格式，不同语言都是用的特殊字符串
# json序列化只支持python部分数据结构：dict,list,tuple,str,int,float,True,False,None
# b. pickle模块：python语言遵守的数据转化格式，只在python中使用
# 支持Python所有的数据类型包括实例化对象
# c. shelve模块：字典操作方式去操作特殊字符串

# 2. json模块：将满足条件的数据结构转换成特殊字符出啊，并且可以反序列化还原回去
# 用于网络传输：dumps，loads
# import json
#
# dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# str_dic = json.dumps(dic)  # 序列化：将一个字典转换成一个字符串
# print(type(str_dic), str_dic)  # <class 'str'> {"k1": "v1", "k2": "v2", "k3": "v3"}
# # json转换完的字符串类型的字典中的字符串是由""表示的
#
# dic2 = json.loads(str_dic)  # 反序列化：将一个字符串格式的字典转换成一个字典
# print(type(dic2), dic2)  # <class 'dict'> {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# # 用json的loads功能处理的字符串类型的字典中的字符串必须由""表示

# list_dic = [1, ['a', 'b', 'c'], 3, {'k1': 'v1', 'k2': 'v2'}]
# str_dic = json.dumps(list_dic)  # 也可以处理嵌套的数据类型
# print(type(str_dic), str_dic)  # <class 'str'> [1, ["a", "b", "c"], 3, {"k1": "v1", "k2": "v2"}]
#
# list_dic2 = json.loads(str_dic)
# print(type(list_dic2),list_dic2)  # <class 'list'> [1, ['a', 'b', 'c'], 3, {'k1': 'v1', 'k2': 'v2'}]
#
# # 用于文件读写：dump，load
# import json
# f = open('test.json', 'w')
# dic = {'k1':'测试1', 'k2':'测试2', 'k3':'测试3'}
# json.dump(dic, f)  # dump方法接收一个文件句柄，直接将字典转换成json字符串写入文件
# f.close()
# # json文件专门存储json字符串
#
# f = open('test.json')
# dic = json.load(f)  # load方法接收一个文件句柄，直接将文件中的json字符串转换成数据结构返回
# f.close()
# print(type(dic), dic)  # <class 'dict'> {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

# 其他参数
# ensure_ascii: 当它为True的时候，所有非ASCII码字符显示为\uXXXX序列，在dump时将ensure_ascii设置为False，存入json的中文即可正常显示
# separators：分隔符，实际上是(item_separator, dict_separator)的一个元组，默认的就是(',',':')表示dictionary内keys之间用','隔开，而KEY和value之间用':'隔开
# sort_keys：将数据根据keys的值进行排序

# json序列化存储多个数据到一个文件
# import json
#
# dic1 = {'name': 'oldboy1'}
# dic2 = {'name': 'oldboy2'}
# dic3 = {'name': 'oldboy3'}
# f = open('序列化.json', encoding='utf-8', mode='a')
# str1 = json.dumps(dic1)
# f.write(str1 + '\n')
# str2 = json.dumps(dic2)
# f.write(str2 + '\n')
# str3 = json.dumps(dic3)
# f.write(str3 + '\n')
# f.close()
#
# f = open('序列化.json', encoding='utf-8')
# for line in f:
#     print(type(line), line)  # <class 'str'>
#     print(json.loads(line))  # {'name': 'oldboy1'}

# 3. pickle模块：将python所有数据结构及对象转换成bytes类型，然后反序列还原
# 用于网络传输：dumps，loads
# import pickle
#
# dic = {'k1': '测试1', 'k2': '测试2', 'k3': '测试3'}
# str_dic = pickle.dumps(dic)
# print(type(str_dic), str_dic)  # bytes类型
#
# dic2 = pickle.loads(str_dic)
# print(type(dic2), dic2)  # 字典 <class 'dict'> {'k1': '测试1', 'k2': '测试2', 'k3': '测试3'}
#
#
# # 序列化对象
# def func():
#     print(666)
#
#
# ret = pickle.dumps(func)
# print(type(ret), ret)
#
# f1 = pickle.loads(ret)  # # f1得到 func函数的内存地址
# f1()  # 执行func函数

# 用于文件读写：dump，load
# import pickle
# dic = {(1, 2): 'oldboy', 1: True, 'set': {1, 2, 3}}
# print(dic)
# f = open('pick序列化', mode='wb')
# res = pickle.dump(dic, f)
# print(type(res), res)
# f.close()
# with open('pick序列化', mode='rb') as f1:
#     res = pickle.load(f1)
#     print(type(res), res)  # <class 'dict'> {(1, 2): 'oldboy', 1: True, 'set': {1, 2, 3}}

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
