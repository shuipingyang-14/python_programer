# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/19 10:02
@ file:     5 装饰器.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# 开放封闭原则：
# 1.对扩展是开放的：任何一个程序，不可能在设计之初就已经想好了所有的功能并且未来不做任何更新和修改，必须允许代码扩展、添加新功能
# 2.对修改是封闭的：写一个函数，很有可能已经交付给其他人使用了，如果这个时候我们对函数内部进行修改，或者修改了函数的调用方式，很有可能影响其他已经在使用该函数的用户

# 装饰器：在不改变原被装饰的函数的源代码以及调用方式下，为其添加额外的功能

# 测试函数执行效率
import time


def index():
    """
    主页页面
    :return:
    """
    time.sleep(1)
    return "hello"


# 第一个版本：index函数除了完成了自己之前的功能，还增加了一个测试执行效率的功能，符合开放原则
# 其次，index函数源码改变了么？没有，但是执行方式改变了，所以不符合封闭原则
def timer_1(f):
    """
    测试函数执行时间
    :param f:
    :return:
    """
    start_time = time.time()
    re = f()
    end_time = time.time()
    print(f'此函数的执行效率为{end_time - start_time}')
    return re


# print(timer_1(index))


# 第二个版本：装饰器
def timer_2(f):
    def inner():
        start_time = time.time()
        f()
        end_time = time.time()
        print(f'此函数的执行效率为{end_time - start_time}')

    return inner


# f = timer_2(index)
# print(f())


# 带返回值的装饰器
def timer_3(f):
    def inner():
        start_time = time.time()
        re = f()
        end_time = time.time()
        print(f'此函数的执行效率为{end_time - start_time}')
        return re

    return inner


# f = timer_3(index)
# print(f())


# 带一个参数的装饰器
def home_1(name):
    time.sleep(1)
    print(f'欢迎访问{name}主页')


def timer_4(f):
    def inner(name):
        start_time = time.time()
        f(name)
        end_time = time.time()
        print(f'此函数的执行效率为{end_time - start_time}')

    return inner


# home = timer_4(home_1)
# home('太白')


# 带多个参数的装饰器

def home_2(name, age):
    time.sleep(1)
    print(f'欢迎访问{name},{age}主页')


def timer_5(f):
    def inner(*args, **kwargs):
        start_time = time.time()
        f(*args, **kwargs)
        end_time = time.time()
        print(f'此函数的执行效率为{end_time - start_time}')

    return inner


# home = timer_5(home_2)
# home('太白', 18)


# 标准装饰器

def wrapper(func):
    def inner(*args, **kwargs):
        """
        执行被装饰函数之前操作
        """
        ret = func(*args, **kwargs)
        """
        执行被装饰函数之后的操作
        """
        return ret

    return inner


def timer(func):  # func = home
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f'此函数的执行效率为{end_time - start_time}')

    return inner


@timer
def home(name, age):
    time.sleep(1)
    print(name, age)
    print(f'欢迎访问{name}主页')


# home('太白', 18)

# 简单版模拟博客园登录
# 需求： 博客园登陆之后有几个页面，diary，comment，home，如果我要访问这几个页面，必须验证我是否已登录
# 如果已经成功登录，那么这几个页面我都可以无阻力访问
# 如果没有登录，任何一个页面都不可以访问，我必须先登录，登录成功之后，才可以访问这个页面

login_status = {
    'username': None,
    'status': False,
}


def auth(func):
    def inner(*args, **kwargs):
        if login_status['status']:
            ret = func(*args, **kwargs)
            return ret
        username = input("请输入用户名：").strip()
        password = input("请输入密码：").strip()

        if username == 'xy' and password == '123':
            login_status['status'] = True
            ret = func(*args, **kwargs)
            return ret

    return inner


@auth
def diary():
    print("欢迎访问日记页面")


@auth
def comment():
    print("欢迎访问评论页面")


@auth
def home():
    print("欢迎访问博客园主页")


# diary()
# comment()
# home()

# 带参数的装饰器
def auth(x):
    def auth2(func):
        def inner(*args, **kwargs):
            if login_status['status']:
                ret = func(*args, **kwargs)
                return ret

            if x == 'wechat':
                username = input("请输入用户名：").strip()
                password = input("请输入密码：").strip()

                if username == 'xy' and password == '123':
                    login_status['status'] = True
                    ret = func(*args, **kwargs)
                    return ret
            elif x == 'qq':
                username = input("请输入用户名：").strip()
                password = input("请输入密码：").strip()

                if username == 'xy' and password == '123':
                    login_status['status'] = True
                    ret = func(*args, **kwargs)
                    return ret

        return inner

    return auth2


@auth('wechat')
def jitter():
    print('记录美好生活')


# @auth('wechat') :分两步：
# 第一步先执行auth('wechat')函数，得到返回值auth2
# 第二步@与auth2结合，形成装饰器@auth2 然后在依次执行


@auth('qq')
def pipefish():
    print('期待你的内涵神评论')


jitter()
pipefish()
