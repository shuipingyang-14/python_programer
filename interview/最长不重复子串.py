# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/29 10:00
@ file:     最长不重复子串.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

def long_no_repeat_substr(strs):
    res_list = []
    if strs == '':
        return 0
    length = len(strs)
    for i in range(length):
        tmp = strs[i]
        for j in range(i + 1, length):
            if str[j] not in tmp:
                tmp += one_str[j]
            else:
                break
        res_list.append(tmp)
    print(res_list)
    max = res_list[0]
    for i in range(1, len(res_list)):
        if len(res_list[i]) > len(max):
            max = res_list[i]
    return max

def lengthOfLongestSubstring(s):
    if s == '':
        return 0
    if len(s) == 1:
        return 1

    def find_left(s, i):
        tmp_str = s[i]
        j = i - 1
        while j >= 0 and s[j] not in tmp_str:
            tmp_str += s[j]
            j -= 1
        return len(tmp_str)

    length = 0
    for i in range(0, len(s)):
        length = max(length, find_left(s, i))
    return length



if __name__ == '__main__':
    one_str_list = ['120135435', 'abdfkjkgdok', '123456780423349']
    for one_str in one_str_list:
        res = long_no_repeat_substr(one_str)
        print('{0}最长非重复子串为：{1}'.format(one_str, res))