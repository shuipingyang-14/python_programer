# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/1 17:37
@ file:     无重复最长字串.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


def lengthOfLongestSubstring(s: str):
    # 字符串为空则返回零
    if not s:
        return 0

    window = []  # 滑动窗口数组
    max_length = 0  # 最长串长度

    # 遍历字符串
    for c in s:
        # 如果字符不在滑动窗口中，则直接扩展窗口
        if c not in window:
            # 使用当前字符扩展窗口
            window.append(c)
        # 如果字符在滑动窗口中，则
        # 1. 从窗口中移除重复字符及之前的字符串部分
        # 2. 再扩展窗口
        else:
            # 从窗口中移除重复字符及之前的字符串部分，新字符串即为无重复字符的字符串
            window[:] = window[window.index(c) + 1:]
            # 扩展窗口
            window.append(c)
        # 更新最大长度
        max_length = max(len(window), max_length)
    return max_length if max_length != 0 else len(s)


if __name__ == '__main__':
    one_str_list = ['120135435', 'abdfkjkgdok', '123456780423349']
    for one_str in one_str_list:
        res = lengthOfLongestSubstring(one_str)
        print('{0}最长非重复子串长度为：{1}'.format(one_str, res))