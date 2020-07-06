# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 22:45
# @python  : python 3.7
# @Author  : 水萍
# @File    : 1 str_operation.py
# @Software: PyCharm


s1 = "python learning"
# 对字符串进行索引，切盼出来的数据类型都是str
# 从左至右有顺序，下标，索引
# 按照索引取值
s2 = s1[0]
print(s2, type(s2))
s3 = s1[-1]
print(s3)

# 按照切片取值
s1 = "python learning"
# 取头不取尾
s2 = s1[0:6]
print(s2)
s3 = s1[:6]
print(s3)
s4 = s1[6:]
print(s4)
# 切片步长(取钱五位数，隔一位取一个)
s5 = s1[:5:2]
print(s5)
# 反序
s6 = s1[::-1]
print(s6)
# 倒序
s7 = s1[-1::-2]
print(s7)
# 正序:
print(s1[:])

# 按索引，s1[index]
# 按切片，s1[start_index:end_index+1]
# 按切片步长，s1[start_index:end_index+1:loop]
# 反向按照切片步长：s1[start_index:end_index后延一位:-1]

# 字符串常用操作
s = 'HellpWorld'
# 1. upper lower
s1 = s.upper()   # 小写变大写
print(s1)
s2 = s.lower()   # 大写变小写
print(s2)

# 应用：
# username = input("用户名：")
# password = input("密码：")
# code = "QweA"
# print("验证码：%s" %code)
# your_code = input("请输入验证码，不区分大小写：")
# if your_code.upper() == code.upper():
# 	if username == "xy" and password == "123":
# 		print("登录成功")
# 	else:
# 		print("用户名或者密码错误")
# else:
# 	print("验证码错误")

# 2. startswith  endswith
s = "hello World"
print(s.startswith("hello", 0, 5))
print(s.endswith("orld", 3, 100))

# 3. replace 替换
msg = 'we are family '
s1 = msg.replace(' ', "%20", 2)   # 默认全部替换。从左至右替换次数
s2 = msg.replace(' ', "%20")
print(s1, s2)

# 4. strip 去字符串首尾空格 \t  \n
s = " we are太白happy "
s1 = s.strip(' ')
print(s1)
# 去除指定字符串
s2 = s1.strip(' warheay')
print(s2)

# 5. split 默认其按照空格分隔，返回一个列表
s = "太白 女神 男神"
ss = "太白-女神-男神"
s1 = s.split()
print(s1)
s2 = ss.split("-")
print(s2)
sss = " :123:1:123"
print(sss.split(":",2))  # 只分隔两次

# 5. join
s = "alex"
s1 = ["太白", "123"]
s2 = "+".join(s1)   # list内的元素必须都是字符串类型
print(s2)

# 6. count 统计字符出现次数
s = "adq2gfuffgb2adqd2"
print(s.count('a'))

# 7. format 格式化输出
msg = "我叫{}今年{}性别{}".format('xy', 18, '女')
print(msg)
msg = "我叫{1}今年{1}性别{2}".format('xy', 18, '女')
print(msg)
msg = "我叫{name}今年{age}性别{sex}".format(name = 'xy', age = 18, sex = '女')
print(msg)

# 8. is系列
s = "12389①2423½"
print(s.isalnum())  # 字符串由字母或者数字组成
print(s.isalpha())  # 字符串只由字母组成
print(s.isdecimal())  # 字符串只由十进制组成
print(s.isdigit())  # 字符串是否只由数字组成
print(s.isnumeric()) # 字符串是否只由数字组成，数字可以是： Unicode 数字，全角数字（双字节），罗马数字，汉字数字，指数类似 ² 与分数类似 ½ 也属于数字

# 9. capitalize
s1 = "taiBai hello"
print(s1.capitalize())  # 首字母变大写，其余变小写

# 10. title
s1 = "taiBai hello3hello"
print(s1.title())   # 每个单词首字母大写

# 11. swapcase
s1 = "TaiBai Hello3hello"
print(s1.swapcase())  # 大小写反转

# 11. center
s1 = "hello"
print(s1.center(20, '*'))  # 以字符串为中心，补充够长度的字符

# 12. find
s1 = 'hello'
print(s1.find('l'))  # 通过元素找索引，找到第一个就返回，找不到返回-1

# 13. index
s1 = 'hello'
print(s1.index('l'))  # 通过元素找索引，找到第一个就返回，找不到报错