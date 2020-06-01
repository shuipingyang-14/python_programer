# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/29 14:43
@ file:     file_operation.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

import os, stat


def access_test():
    res = os.access(r"E:\PyCode\python_programer\dir_operation", os.F_OK)
    print("此目录是否存在：%s" % res)

    res = os.access(r"E:\PyCode\python_programer\dir_operation", os.R_OK)
    print("此目录是否可读：%s" % res)

    res = os.access(r"E:\PyCode\python_programer\dir_operation", os.W_OK)
    print("此目录是否可写：%s" % res)

    res = os.access(r"E:\PyCode\python_programer\dir_operation", os.X_OK)
    print("此目录是否可执行：%s" % res)


def chdir_test():
    path = "../"
    res = os.getcwd()  # 查看当前工作目录
    print("当前工作目录为：%s" % res)
    # 修改当前工作目录
    os.chdir(path)
    # 查看修改后的目录
    res = os.getcwd()
    print("修改后的工作目录为：%s" % res)


def chmod_test():
    # 假定当前文件可以通过用户组执行
    os.chmod(".", stat.S_IXGRP)

    # 设置文件可以被其他用户写入
    os.chmod(".", stat.S_IWOTH)

    print("修改成功")


def chown_test():
    os.chmod(".", 100, -1)
    print("修改成功")


def getcwd_test():
    # 切换到上级目录
    os.chdir(r"E:\PyCode\python_programer\python_learn\day_4")

    # 打印当前目录
    print("当前工作目录：%s" % os.getcwd())

    # 打开 "/tmp"
    fd = os.open("test.txt", os.O_RDONLY)

    # 使用 os.fchdir() 方法修改目录
    # os.fchdir(fd)

    # 打印当前目录
    print("当前工作目录 : %s" % os.getcwd())

    # 关闭文件
    os.close(fd)


def listdir_test():
    path = r"E:\PyCode\python_programer\python_learn"
    dir = os.listdir(path)

    for file in dir:
        print(file)


def mkdir_test():
    path = "test"
    os.mkdir(path, 755)
    print("目录已创建")


if __name__ == '__main__':
    # access_test()
    # chdir_test()
    # chmod_test()
    # chown_test()
    # getcwd_test()
    # listdir_test()
    mkdir_test()
