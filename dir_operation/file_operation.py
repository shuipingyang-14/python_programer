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


def open_test():
    # 打开文件
    fd = os.open("foo.txt", os.O_RDWR | os.O_CREAT)

    # 写入字符串
    os.write(fd, 'This is test')

    # 关闭文件
    os.close(fd)

    print("关闭文件成功!!")


def read_test():
    # 打开文件
    fd = os.open("foo.txt", os.O_RDWR)

    # 读取文本
    ret = os.read(fd, 1024)
    print(ret)

    # 关闭文件
    os.close(fd)
    print("关闭文件成功!!")


def remove_test():
    print("删除前目录为: %s" % os.listdir(os.getcwd()))
    os.remove("foo.txt")
    print("删除后目录为: %s" % os.listdir(os.getcwd()))

    os.remove(r"E:\PyCode\python_programer\python_learn\day_4")


def removedirs_test():
    # 列出目录
    print("目录为: %s" % os.listdir(os.getcwd()))

    # 移除
    os.removedirs("/test")

    # 列出移除后的目录
    print("移除后目录为 %s :" % os.listdir(os.getcwd()))


def rename_test():
    # 列出目录
    print("目录为: %s" % os.listdir(os.getcwd()))

    # 重命名
    os.rename("目录操作.md", "目录操作.md")

    print("重命名成功。")

    # 列出重命名后的目录
    print("目录为: %s" % os.listdir(os.getcwd()))


def renames_test():
    print("当前目录为: %s" % os.getcwd())

    # 列出目录
    print("目录为: %s" % os.listdir(os.getcwd()))

    # 重命名 "aa1.txt"
    os.renames("aa.txt", "newdir/aanew.txt")

    print("重命名成功。")

    # 列出重命名的文件 "aa1.txt"
    print("目录为: %s" % os.listdir(os.getcwd()))


def rmdir_test():
    # 列出目录
    print("目录为: %s" % os.listdir(os.getcwd()))

    # 删除路径
    os.rmdir("test")

    # 列出重命名后的目录
    print("目录为: %s" % os.listdir(os.getcwd()))


def stat_test():
    statinfo = os.stat('file_operation.py')
    print(statinfo)


def write_test():
    # 打开文件
    fd = os.open("newdir\\aanew.txt", os.O_RDWR | os.O_CREAT)

    # 写入字符串
    ret = os.write(fd, "This is runoob.com site")

    # 输入返回值
    print("写入的位数为: %s" % ret)

    # 关闭文件
    os.close(fd)
    print("关闭文件成功!!")


if __name__ == '__main__':
    # access_test()
    # chdir_test()
    # chmod_test()
    # chown_test()
    # getcwd_test()
    # listdir_test()
    # mkdir_test()
    # open_test()
    # read_test()
    # remove_test()
    # removedirs_test()
    # rename_test()
    # renames_test()
    # rmdir_test()
    # stat_test()
    write_test()
