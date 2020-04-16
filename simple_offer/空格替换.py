# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 23:23
# @python  : python 3.7
# @Author  : 水萍
# @File    : 空格替换.py
# @Software: PyCharm


def replace_space(s: str) -> str:
	# return s.replace(' ', '%20')
	res = ''
	for c in s:
		if c == ' ':
			res += '%20'
		else:
			res += c
	return res


if __name__ == "__main__":
	res = replace_space("we are family")
	print(res)