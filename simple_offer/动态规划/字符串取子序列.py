# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/24 17:46
@ file:     字符串取子序列.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# 给出一个字符串S，牛牛想知道这个字符串有多少个子序列等于"niuniu"
# 子序列可以通过在原串上删除任意个字符(包括0个字符和全部字符)得到

def str_change(s):
    count = [0 for i in range(6)] # 统计'n','ni','niu','niun','niuni','niuniu'

    for i in s:
        if i == 'n':
            count[0] += 1
            count[3] += count[2]
        if i == 'i':
            count[1] += count[0]
            count[4] += count[3]
        if i == 'u':
            count[2] += count[1]
            count[5] += count[4]

    print(count)
    return count[5]


if __name__ == '__main__':
    s = "niuninniniiu"
    print(str_change(s))