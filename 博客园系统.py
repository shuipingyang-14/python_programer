# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 19:20
# @python  : python 3.7
# @Author  : 水萍
# @File    : 博客园系统.py
# @Software: PyCharm

msg = """
1 请登录
2 请注册
3 进入文章页面
4 进入评论页面
5 进入日记页面
6 进入收藏页面
7 注销账号
8 退出整个程序
"""


def register():
    """
    注册账号
    用户名和密码记录在文件中
    用户名只能含有字母或者数字（不包含特殊字符，保证用户名唯一）
    密码长度在6-14个字符
    超过三次登录失败，退出整个程序
    :return:
    """
    pass


def login():
    """
    登录账号
    用户输入用户名妈妈进行登录验证
    登录成功后，才可访问3-7选项
    :return:
    """
    pass


def arctile():
    """
    文章页面
    提示：欢迎xx进入文章页面
    用户可选择：直接写入内容，还是导入md文件
    如果直接写内容，文件名|文件内容...最后创建文章
    如果导入md，用户输入md文件路径，将此文件内容写入文章
    :return:
    """
    pass


def comment():
    """
    评论页面
    提示：欢迎xx进入评论页面
    :return:
    """
    pass


def diary():
    """
    日记页面
    提示：欢迎xx进入日记页面
    :return:
    """
    pass


def favorite():
    """
    收藏页面
    提示：欢迎xx进入收藏页面
    :return:
    """
    pass


def logout():
    """
    注销账号
    将已经登录的状态变成未登录状态（访问3-7重新登录）
    :return:
    """
    pass


def quit():
    """
    退出程序
     :return:
    """
    pass