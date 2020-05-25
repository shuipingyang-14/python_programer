# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/22 22:45
@ file:     公共前缀.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


def longestCommonPrefix(strs):
    res = ''
    if strs == []:
        return res
    for i in range(len(strs[0])):
        index = 0
        j = len(strs) - 1
        while index < j:
            l1 = len(strs[index])
            l2 = len(strs[index+1])
            if i < l1 and i < l2:
                t1 = strs[index][i]
                t2 = strs[index + 1][i]
            elif i >= l1:
                t1 = ''
                t2 = strs[index + 1][i]
            elif i >= l2:
                t2 = ''
                t1 = strs[index][i]
            if t1 == t2:
                index += 1
            else:
                break
        if index == j:
            res += strs[0][i]
        else:
            break
    return res


if __name__ == '__main__':
    l = ["cba",""]
    res = longestCommonPrefix(l)
    print(res)
