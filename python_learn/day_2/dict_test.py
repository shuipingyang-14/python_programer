# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 17:05
# @python  : python 3.7
# @Author  : 水萍
# @File    : dict_test.py
# @Software: PyCharm

# 电影投票
l = ["复仇者联盟4", "前任攻略3", "大话西游", "卧虎藏龙"]

dic = dict.fromkeys(l, 0)
print(dic)  # 初始票数

while 1:
    for index, movie_name in enumerate(l):
        print(f"序号：{index+1}, 电影名称：{movie_name}")
    num = input("请输入喜欢的电影序号：").strip()
    if num.isdecimal():
        num = int(num)
        if 0 < num <= len(l):
            if l[num-1] not in dic:
                dic[l[num-1]] = 1
            else:
                dic[l[num-1]] += 1
        else:
            print("超出范围，请重新输入")
    elif num.upper() == 'Q':
        break
    else:
        print("请输入数字")

print(dic)