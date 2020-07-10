# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 17:45
# @python  : python 3.7
# @Author  : 水萍
# @File    : list_test.py
# @Software: PyCharm

l1 = [
    {"name": "alex", "hobby": "study"},
    {"name": "alex", "hobby": "dance"},
    {"name": "alex", "hobby": "read"},
    {"name": "bray", "hobby": "study"},
    {"name": "bray", "hobby": "dance"},
    {"name": "siri", "hobby": "study"},
    {"name": "siri", "hobby": "read"},
    {"name": "alex", "hobby": "swim"},
    {"name": "bray", "hobby": "swim"}
]

l2 = [
    {"name": "alex", "hobby": ["study", "dance", "read", "swim"]},
    {"name": "bray", "hobby": ["study", "dance"]},
    {"name": "siri", "hobby": ["study", "read"]}
]

# 把相同元素集合处理
# 直接构建
l = []
for i in l1:
    for j in l:
        if i["name"] == j["name"]:
            j["hobby"].append(i["hobby"])
            break
    else:
        l.append({"name":i["name"], "hobby":[i["hobby"]]})

print(l)

# dict构建
dic = {}
for i in l1:
    if i["name"] not in dic:
        dic[i["name"]] = {"name":i["name"], "hobby":[i["hobby"],]}
    else:
        dic[i["name"]]["hobby"].append(i["hobby"])

print(list(dic.values()))