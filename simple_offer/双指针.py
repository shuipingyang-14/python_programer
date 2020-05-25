# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/22 22:17
@ file:     双指针.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

def maxArea(l):
    i = 0
    j = len(l)-1
    ret = 0
    while i<j:
        area = (j-i)*min(l[i], l[j])
        if ret < area:
            ret = area
        if l[i] < l[j]:
            i += 1
        else:
            j -= 1
    return ret



if __name__ == '__main__':
    l = [1,8,6,2,5,4,8,3,7]
    ret = maxArea(l)
    print(ret)