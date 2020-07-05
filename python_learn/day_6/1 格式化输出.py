# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/26 10:43
@ file:     1 格式化输出.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

name = "水萍"
age = 18
sex = '女'
msg = F'姓名:{name} 性别:{sex} 年龄:{age}'
print(msg)
msg = f'姓名:{name} 性别:{sex} 年龄:{age}'
print(msg)

# 加入表达式
print(f'{3*32}')
name = 'barry'
print(f'全部大写：{name.upper()}')

# 字典
teacher = {'name':'barry', 'age':18}
msg = f'The teacher is {teacher["name"]}, aged {teacher["age"]}'
print(msg)

# 列表
l1 = ['barry', 18]
msg = f'姓名：{l1[0]}, 年龄：{l1[1]}'
print(msg)

# 表达式
def sum(a, b):
    return a +b

a = 1
b = 2
print("求和的结果为："+ f'{sum(a,b)}')

# 多行
name = 'barry'
age = 18
ajd = 'handsome'
speaker = f'Hi {name}.'\
    f'Yor are {age} years old.'\
    f'You are a {ajd} guy.'
print(speaker)