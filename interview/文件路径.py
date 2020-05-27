# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/26 11:01
@ file:     文件路径.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""


def print_directory_content(spath):
    """
    :param path: 文件夹的名称
    :return: 返回该文件夹中文件的路径, 以及其包含文件夹中文件的路径
    """
    import os
    print(os.listdir(spath))
    for index in os.listdir(spath):
        child_path = os.path.join(spath, index)
        if os.path.isdir(child_path):
            print_directory_content(child_path)
        else:
            print(child_path)


if __name__ == '__main__':
    path = "E:\PyCode\python_programer\python_learn"
    print_directory_content(path)
