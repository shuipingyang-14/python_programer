# -*- coding: utf-8 -*-
# @Time    : 2020/5/1 22:43
# @python  : python 3.7
# @Author  : 水萍
# @File    : 2 格式化.py
# @Software: PyCharm


# 格式化输出
# name = input("请输入你的姓名：")
# age = input("请输入你的年龄：")
# job = input("请输入你的工作：")
# hobby = input("请输入你的爱好：")
#
# msg = """--- info of %s ---
# Name  : %s
# Age   : %s
# Job   : %s
# Hobby : %s
# --- end ---""" %(name, name, age, job, hobby)
# print(msg)

msg = "我叫%s, 今年%s, 学习进度1%%" %("xy", 18)
print(msg)

msg = "我叫{}, 今年{}, 学习进度1%".format("xy", 18)
print(msg)