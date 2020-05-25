# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/25 17:51
@ file:     price.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""
sum = 0
result = []
dic = {}
f = open("test_price.txt")
for line in f:
    line = line.strip("\n")
    res = line.split(' ')
    dic["name"] = res[0]
    dic["price"] = res[1]
    dic["amount"] = res[2]
    sum += int(res[1]) * int(res[2])
    result.append(dic)
print(result)
print(sum)
f.close()