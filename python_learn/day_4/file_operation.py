# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/25 16:58
@ file:     file_operation.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# f = open('test.txt', mode='r', encoding='utf-8')
"""
 f: 就是一个变量，一般都会将它写成f,f_obj,file,f_handler,fh,等，它被称作文件句柄
 'test.txt': 这个是文件的路径
 mode： 定义操作方式：r为读模式
 encoding: 不是具体的编码或者解码，他就是声明：此次打开文件使用什么编码本
 一般来说：你的文件用什么编码保存的，就用什么方法打开，一般都是用utf-8（有些使用的是gbk）
"""
# content = f.read()
# f.read(): 操作文件，比如读文件，给文件写内容，等等，都必须通过文件句柄进行操作
# print(content)
# f.close()
# f.close(): 关闭文件句柄（可以把文件句柄理解成一个空间，这个空间存在内存中，必须要主动关闭）


# 1. r方式读文件
# 1.1 read()
# 以只读方式打开文件，文件的指针将会放在文件的开头
# 是文件操作最常用的模式，也是默认模式，如果一个文件不设置mode，那么默认使用r模式操作文件
# f = open('test.txt', mode='r', encoding='utf-8')
# msg1 = f.read(2)
# msg = f.read()
# ead()将文件中的内容全部读取出来
# 弊端 如果文件很大就会非常的占用内存,容易导致内存奔溃
# read()读取的时候指定读取到什么位置, 在r模式下,n按照字符读取
# f.close()
# print(msg1)
# print(msg)

# 1.2 readline()
# readline()读取每次只读取一行
# readline()读取出来的数据在后面都有一个\n
# f = open("test.txt", 'r', encoding='utf-8')
# msg1 = f.readline().strip()
# strip去掉结尾的换行符
# msg2 = f.readline().strip()
# f.close()
# print(msg1)
# print(msg2)

# 1.3 readlines()
#  readlines() 返回一个列表，列表里面每个元素是原文件的每一行，如果文件很大，占内存，容易崩盘
# f = open('test.txt', encoding='utf-8')
# print(f.readlines())
# f.close()

# 1.4 for循环
# f = open('test.txt','r',encoding='utf-8')
# for line in f:
#     print(line.strip())      #这种方式就是在一行一行的进行读取
# f.close()

# 2. rb方式读文件
# 以二进制格式打开一个文件用于只读，文件指针在文件的开头
# f = open('test.jpg', 'rb')
# content = f.read()
# print(content)
# f.close()

# 3. w方式
# 如果文件不存在，利用w模式操作文件，那么它会先创建文件，然后写入内容
f = open("test_1.txt", 'w')
f.write("hello world")
f.close()
# 如果文件存在，利用w模式操作文件，先清空原文件内容，在写入新内容
f = open("test.txt", 'w')
f.write("hello wirld 你好")
f.flush()  # 强制保存
f.close()

# 4. wb方式
# wb模式：以二进制格式打开一个文件只用于写入
# 如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除
# 如果该文件不存在，创建新文件。一般用于非文本文件如：图片，音频，视频等
#
# 举例说明：
# 以rb的模式将一个图片的内容以bytes类型全部读取出来，然后在以wb将全部读取出来的数据写入一个新文件，这样我就完成了类似于一个图片复制的流程
# f = open('test.jpg', 'rb')
# content = f.read()
# print(content)
# f.close()
# f1 = open("test_2.jpg", 'rb')
# f1.write(content)
# f1.close()

# 5. a方式
# 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾
# 新的内容将会被写入到已有内容之后
# 如果该文件不存在，创建新文件进行写入
# 如果文件不存在，利用a模式操作文件，那么它会先创建文件，然后写入内容
# f = open("test_11.txt", encoding='utf-8', mode='a')
# f.write("增加新内容1\n")
# f.close()
# 如果文件存在，利用a模式操作文件，那么它会在文件的最后面追加内容
# f = open("test_11.txt", encoding='utf-8', mode='a')
# f.write("增加新内容2")
# f.close()

# 6. r+方式
# r+: 打开一个文件用于读写。文件指针默认将会放在文件的开头
# f = open("test_1.txt", encoding='utf-8', mode='r+')
# content = f.read()
# print(content)
# f.write("\n追加内容")
# 如果在读写模式下，先写后读，那么文件就会出问题，因为默认光标是在文件的最开始，你要是先写，则写入的内容会讲原内容覆盖掉，直到覆盖到你写完的内容，然后在后面开始读取

# 7. 其他功能
# 7.1 read(n)
# 1. 文件打开方式为文本模式时，代表读取n个字符
# 2. 文件打开方式为b模式时，代表读取n个字节

# 7.2 seek()
# seek(n)光标移动到n位置,注意: 移动单位是byte,所有如果是utf-8的中文部分要是3的倍数
# 移动到开头:seek(0)
# 移动到结尾:seek(0,2) seek的第二个参数表示的是从哪个位置进行偏移,默认是0,表示开头,1表示当前位置,2表示结尾
# f = open('test_11.txt', mode='r+', encoding='utf-8')
# f.seek(0)  # 光标移动到开头
# content1 = f.read()  # 读取内容, 此时光标移动到结尾
# print(content1)
# f.seek(0) # 再次将光标移动到开头
# f.seek(0, 2) # 将光标移动到结尾
# content2 = f.read() # 读取内容. 什么都没有
# print(content2)
# f.seek(0) # 移动到开头
# f.write("张国荣") # 写入信息. 此时光标在9 中文3 * 3个 = 9
# f.flush()
# f.close()

# 7.3 tell()
# 获取当前光标在什么位置
# f = open("test_11.txt", mode="r+", encoding="utf-8")
# f.seek(0) # 光标移动到开头
# content = f.read() # 读取内容, 此时光标移动到结尾
# print(content)
# f.seek(0) # 再次将光标移动到开头
# f.seek(0, 2) # 将光标移动到结尾
# content2 = f.read() # 读取内容. 什么都没有
# print(content2)
# f.seek(0) # 移动到开头
# f.write("张国荣") # 写入信息. 此时光标在9 中⽂文3 * 3个 = 9
# print(f.tell()) # 光标位置9
# f.flush()
# f.close()

# 7.4 readable(), writeable()
# f = open('test_1.txt',encoding='utf-8',mode='r')
# print(f.readable())  # True
# print(f.writable())  # False
# content = f.read()
# f.close()

# 8. 打开文件
# 8.1. 利用with上下文管理这种方式，它会自动关闭文件句柄
# with open('test_1.txt', encoding='utf-8') as f1:
#     f1.read()

# 8.2. 一个with 语句可以操作多个文件，产生多个文件句柄
# with open('test_1.txt', encoding='utf-8') as f1, \
#         open('test_11.txt', encoding='utf-8', mode='w') as f2:
#     f1.read()
#     f2.write('老男孩老男孩')

# 9. 文件修改
# 9.1 将硬盘存放的该文件的内容全部加载到内存，在内存中是可以修改的，修改完毕后，再由内存覆盖到硬盘（word，vim，nodpad++等编辑器）
# import os
#
# with open("test.txt") as read_f, open(".test.txt.swap", 'w') as write_f:
#     data = read_f.read()    # 全部读入内存,如果文件很大,会很卡
#     data = data.replace("hello", 'SS  ')   # 在内存中完成修改
#     write_f.write(data)  # 一次性写入新文件
#
# os.remove("test.txt")
# os.rename('.test.txt.swap','test.txt')   #将新建的文件重命名为原文件

# 9.2 将硬盘存放的该文件的内容一行一行地读入内存，修改完毕就写入新文件，最后用新文件覆盖源文件
import os

with open('test_11.txt', 'r', encoding='utf-8') as read_f,open('.test_11.txt.swap','w', encoding='utf-8') as write_f:
    for line in read_f:
        line=line.replace('hello','alex')
        write_f.write(line)

os.remove('test_11.txt')
os.rename('.test_11.txt.swap','test_11.txt')