# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/5 12:50
@ file:     9 shutil模块.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

import shutil
# 1. 文件内容拷贝
shutil.copyfileobj(open('test.txt', 'r'), open('test1.txt', 'w'))
# 2. 文件拷贝
shutil.copyfile('test.log', 'f2.log') # 目标文件不需要存在
# 3. 拷贝权限，内容，组用户不变
shutil.copymode('test.log', 'f2.log') # 目标文件必须存在
# 4. 拷贝状态的信息，包括：mode bits, atime, mtime, flags
shutil.copystat('test.log', 'f2.log') # 目标文件必须存在
# 5. 拷贝文件和权限
shutil.copy('test.log', 'f2.log')
# 6. 拷贝文件和状态信息
shutil.copy2('test.log', 'f2.log')
# 7. 递归拷贝文件
# shutil.copytree('folder1', 'folder2', ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))
# 目标目录不能存在，注意对folder2目录父级目录要有可写权限，ignore的意思是排除
# 8. 递归删除文件
# shutil.rmtree('folder1')
# 9. 递归移动文件
# shutil.move('folder1', 'folder3')
# 10. 创建压缩包并返回文件路径
"""
base_name：压缩包文件名，可以是压缩包路径，只是文件名保存在当前目录，否则保存指定路径
format：压缩包种类：zip, tar, bztar, gztar
root_dir：要压缩的文件夹路径（默认当前目录）
owner：用户，默认当前用户
group；组，默认当前组
logger：用于记录日志，通常是logging.Logger对象
"""

# 将 /data 下的文件打包放置当前程序目录
import shutil

ret = shutil.make_archive("9 shutil模块.py", 'gztar', root_dir='../day_8')

# 将 /data下的文件打包放置 /tmp/目录

# ret = shutil.make_archive("/tmp/data_bak", 'gztar', root_dir='/data')

# zipfile
# 压缩
import zipfile
z = zipfile.ZipFile('laxi.zip', 'w')
z.write('test.log')
z.write('test.txt')
z.close()

# 解压
z =zipfile.ZipFile('laxi.zip', 'r')
z.extractall(path='.')
z.close()

# tarfile
# 压缩
import tarfile
t = tarfile.open("test.tar", 'w')
t.add('test.log')
t.add('test.txt')
t.close()

# 解压
t = tarfile.open('test.tar', 'r')
t.extractall(path='.')
t.close()