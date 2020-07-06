# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/1 10:41
@ file:     1 模块.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# 1. 模块简单介绍
# 模块是文件，存放常用的函数，常用功能的集合体
# 模块分类：
# a. 内置模块，也称标准库，python解释器提供，比如time，os模块等
# b. 第三方模块，第三方库，通过pip install安装的模块
# c. 自定义模块，自己定义的一些模块

# 2. import使用
# 模块可包含执行的语句和函数的定义，语句目的是初始化模块，在模块名第一次import语句才执行
# import 语句可以在程序任意位置使用，针对同一个模块import多次，python解释器在第一次导入后就将模块名加载到内存，后续import只是对加载到内存中的模块对象增加因哟个，不会重新执行模块内语句

# import module_test
# import module_test
# import module_test  # 只打印一次 from the module_test.py...

# 导入模块执行的操作：
# a. 创建一个以模块名命名的名称空间
# b. 执行这个名称空间（即导入的模块）里面的代码
# c. 通过模块名.的方式引用模块里面的内容（变量，函数名，类名等）
# 被导入模块有独立的名称空间
# 每个模块都是一个独立的名称空间，定义在这个模块中的函数，把这个模块的名称空间当作全局名称空间

# name = 'alex'
# print(name)  # alex
# print(module_test.name)  # xy
#
# def read1():
#     print(666)
#
# module_test.read1()  # module_test模块： xy
#
# name = '水萍'
# module_test.change()
# print(name)  # 水萍
# print(module_test.name)  # ysp

# 3. 模块操作
# 为模块起别名
# import module_test as mt
# mt.read1()  # module_test模块： ysp

# 导入多个模块
import os, sys, json

# 4. from...import使用
# from module_test import name, read1
# print(name)  # ysp
# read1()  # module_test模块： ysp

# 使用from ... import ... 是将spam中的名字直接导入到当前的名称空间中，所以在当前名称空间中，直接使用名字就可以了、无需加前缀：tbjx.
# from...import...的方式有好处也有坏处
# 好处：使用起来方便了
# 坏处：容易与当前执行文件中的名字冲突
# 执行文件有与模块同名的变量或者函数名，会有覆盖效果
# name = 'oldboy'
# from module_test import name, read1, read2
# print(name)  # ysp
#
# from module_test import name, read1, read2
# name = 'oldboy'
# print(name)   # oldboy
#
# def read1():
#     print(666)
# from module_test import name, read1, read2
# read1()  # module_test模块： ysp
#
# from module_test import name, read1, read2
# def read1():
#     print(666)
# read1()  # 666

# 当前位置直接使用read1和read2，执行仍然以module_test文件全局名称空间
# 导入的函数read1，module_test.py中寻找全局变量 name
# from module_test import read1
# name = 'alex'
# read1()   # from the module_test.py...   module_test模块： xy

# 导入的函数read2，执行时需要调用read1(),仍然回到module_test.py中找read1()
# from module_test import read2
# def read1():
#     print('==========')  # from the module_test.py...    module_test模块
# read2()   # module_test模块： xy

# 5. from ... import * 把模块中所有不是以_开头的名字都导入到当前位置
# 大部分情况下我们的python程序不应该使用这种导入方式，因为*不知道你导入什么名字，很有可能会覆盖掉你之前已经定义的名字，而且可读性极其的差，在交互式环境中导入时没有问题
# 可以使用all来控制*（用来发布新版本），在module_test.py中新增一行
# __all__=['name','read1'] #这样在另外一个文件中用from ... import *就这能导入列表中规定的两个名字

# 6. pY文件功能：
# a. 脚本：一个文件就是一个程序，用来被执行
# b. 模块：文件中存放一堆功能，用来被导入使用

# 控制.py文件在不同的应用场景下执行不同的逻辑（或者是在模块文件中测试代码）
# from module_test import *

# if __name__ == '__main__':
#     read1()   # from the module_test.py...   module_test模块： xy

# 模块的搜索路径 : 内存中已经加载的模块->内置模块->sys.path路径中包含的模块
# 先从内存中已经加载的模块进行寻找，找不到再从内置模块中寻找，内置模块中没有，去sys.path中路径包含的模块中寻找

print(sys.path)
