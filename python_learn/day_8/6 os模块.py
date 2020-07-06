# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/5 13:15
@ file:     6 os模块.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

import os

# 当前执行这个py文件的工作目录相关的工作路径
print(os.getcwd()) # 获取当前工作目录，当前脚本工作目录
# D:\pycode\python_programer\python_learn\day_8
os.chdir('D:')  # 改变当前脚本工作目录
print(os.curdir)  # 返回当前目录 .
print(os.pardir)  # 获取当前目录的父目录字符串名 ..

# 和文件夹相关
# os.makedirs('dirname1/dirname2') # 生成多层递归目录
# os.removedirs('dirname1') # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.mkdir('dirname')    # 生成单级目录；相当于shell中mkdir dirname
# os.rmdir('dirname')    # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
print(os.listdir('dirname'))   # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印

# 和文件相关
# os.remove('test1.txt')   # 删除一个文件
# os.rename("test2.txt","test.txt")  # 重命名文件/目录
print(os.stat('dirname1/dirname2'))  # 获取文件/目录信息
# os.stat_result(st_mode=16895, st_ino=281474976759161, st_dev=3301226793, st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1593926795, st_mtime=1593926512, st_ctime=1593926512)
"""
stat 结构:

st_mode: inode 保护模式
st_ino: inode 节点号
st_dev: inode 驻留的设备
st_nlink: inode 的链接数
st_uid: 所有者的用户ID
st_gid: 所有者的组ID
st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据
st_atime: 上次访问的时间
st_mtime: 最后一次修改的时间
st_ctime: 由操作系统报告的"ctime"在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）
"""


# 和操作系统差异相关
print(os.sep)    # 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
# \
print(os.linesep)    # 输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
# \t\n
print(os.pathsep)    # 输出用于分割文件路径的字符串 win下为;,Linux下为:
# ;
print(os.name)    # 输出字符串指示当前使用平台win->'nt'; Linux->'posix'
# nt


# 和执行系统命令相关
# os.system("bash command")  # 运行shell命令，直接显示
# os.popen("bash command).read()  # 运行shell命令，获取执行结果
print(os.environ)  # 获取系统环境变量
# environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\zsx\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'LAPTOP-80SDJQL0', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'GOPATH': 'C:\\Users\\zsx\\go', 'GOROOT': 'D:\\Go', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\zsx', 'LOCALAPPDATA': 'C:\\Users\\zsx\\AppData\\Local', 'LOGONSERVER': '\\\\LAPTOP-80SDJQL0', 'NUMBER_OF_PROCESSORS': '12', 'ONEDRIVE': 'C:\\Users\\zsx\\OneDrive', 'ONEDRIVECONSUMER': 'C:\\Users\\zsx\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'D:\\软件\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;D:\\Go\\bin;D:\\Git\\cmd;D:\\python3.8\\Scripts\\;D:\\python3.8\\;C:\\Users\\zsx\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\zsx\\go\\bin;D:\\PyCharm 2019.1.1\\bin;C:\\Users\\zsx\\AppData\\Local\\GitHubDesktop\\bin', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'x86', 'PROCESSOR_ARCHITEW6432': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 165 Stepping 2, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': 'a502', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files (x86)', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM': 'D:\\PyCharm 2019.1.1\\bin;', 'PYCHARM_DISPLAY_PORT': '51981', 'PYCHARM_HOSTED': '1', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'D:\\pycode;D:\\PyCharm 2019.1.1\\helpers\\pycharm_matplotlib_backend;D:\\PyCharm 2019.1.1\\helpers\\pycharm_display', 'PYTHONUNBUFFERED': '1', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\zsx\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\zsx\\AppData\\Local\\Temp', 'USERDOMAIN': 'LAPTOP-80SDJQL0', 'USERDOMAIN_ROAMINGPROFILE': 'LAPTOP-80SDJQL0', 'USERNAME': 'zsx', 'USERPROFILE': 'C:\\Users\\zsx', 'WINDIR': 'C:\\Windows'})

#path系列，和路径相关
print(os.path.abspath('6 os模块.py')) # 返回path规范化的绝对路径
# D:\pycode\python_programer\python_learn\day_8\6 os模块.py
print(os.path.split('D:\pycode\python_programer\python_learn\day_8\6 os模块.py')) # 将path分割成目录和文件名二元组返回
# ('D:\\pycode\\python_programer\\python_learn\\day_8', '6 os模块.py')
print(os.path.dirname(os.path.abspath('6 os模块.py'))) # 返回path的目录其实就是os.path.split(path)的第一个元素
# D:\pycode\python_programer\python_learn\day_8
print(os.path.basename(os.path.abspath('6 os模块.py'))) # 返回path最后的文件名如何path以／或\结尾，那么就会返回空值，即os.path.split(path)的第二个元素
# 6 os模块.py
print(os.path.exists(os.path.abspath('6 os模块.py')))  # 如果path存在，返回True；如果path不存在，返回False
# True
print(os.path.isabs('6 os模块.py'))  # 如果path是绝对路径，返回True
# False
print(os.path.isabs(os.path.abspath('6 os模块.py')))
# True
print(os.path.isfile('6 os模块.py'))  # 如果path是一个存在的文件，返回True否则返回False
# True
print(os.path.isdir('D:\pycode\python_programer\python_learn\day_8'))  # 如果path是一个存在的目录，则返回True否则返回False
# True
print(os.path.join('D:\pycode\python_programer\python_learn\day_8', 'test.txt'))  # 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# D:\pycode\python_programer\python_learn\day_8\test.txt
print(os.path.getatime('D:\pycode\python_programer\python_learn\day_8'))  # 返回path所指向的文件或者目录的最后访问时间
# 1593927593.505219
print(os.path.getmtime('D:\pycode\python_programer\python_learn\day_8'))  # 返回path所指向的文件或者目录的最后修改时间
# 1593927629.787524
print(os.path.getsize('D:\pycode\python_programer\python_learn\day_8')) # 返回path的大小
# 4096