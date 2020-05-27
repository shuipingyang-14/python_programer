# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/26 10:54
@ file:     文件操作.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


# 读取文件,大小为10k
def get_lines_1():
    with open("file.txt", 'rb') as f:
        return f.readlines()


# 读取文件，大小为10g
def get_lines_2():
    with open("file.txt", 'rb') as f:
        for i in f:
            yield f


from mmap import mmap


def get_lines_3(fp):
    with open(fp, 'r+') as f:
        m = mmap(f.fileno(), 0)
        tmp = 0
        for i, char in enumerate(m):
            if char == b"\n":
                yield m[tmp:i + 1].decode()
                tmp = i + 1


def process(e):
    print(e)


if __name__ == '__main__':
    for e in get_lines_1():
        process(e)  # 处理每一行数据
    for i in get_lines_3("fp_some_huge_file"):
        print(i)
