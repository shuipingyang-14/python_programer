# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/28 15:51
@ file:     链表相交.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

def get_intersect_node(l1, l2):
    """
    查找相交链表第一个交点
    :param l1:
    :param l2:
    :return:
    """
    len1 = len(l1)
    len2 = len(l2)

    if len1 >= len2:
        for i in range(0, len2):
            if l1[i+len1-len2] == l2[i]:
                return l2[i]
        return None
    else:
        for i in range(0, len1):
            if l2[i+len2-len1] == l1[i]:
                return l1[i]
        return None

if __name__ == '__main__':
    l1 = ['a1','a2', 'a3', 'c1', 'c2','c3']
    l2 = ['b1', 'b2', 'c2', 'c3']

    print(get_intersect_node(l1, l2))
