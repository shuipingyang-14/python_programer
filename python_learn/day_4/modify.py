# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/25 18:04
@ file:     modify.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""
import os


with open("file.txt", encoding='utf-8') as read_f, open(".file.txt.swap", 'w', encoding='utf-8') as write_f:
    data = read_f.read()    # 全部读入内存,如果文件很大,会很卡
    data = data.replace("alex", 'SS')   # 在内存中完成修改
    write_f.write(data)  # 一次性写入新文件

os.remove("file.txt")
os.rename(".file.txt.swap", "file.txt")