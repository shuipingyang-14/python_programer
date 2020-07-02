# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/1 18:57
@ file:     shelve序列化模块.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""
# shelve模块：提供一个open方法，使用key来访问，和字典类似
import shelve

f = shelve.open('shelve_file')
f['key'] = {'int':10, 'float':9.5, 'string':'Sample data'}  #直接对文件句柄操作，就可以存入数据
f.close()

f1 = shelve.open('shelve_file')
existing = f1['key']
f1.close()
print(existing)

# 不支持多个应用同一时间往同一个db进行写操作
# 只进行读操作，可以让shelve通过只读方式打开db
f2 = shelve.open('shelve_file', 'r')
existing = f2['key']
f1.close()
print(existing)

# shelve在默认情况下是不会记录待持久化对象的任何修改的，在shelve.open()时候需要修改默认参数，否则对象的修改不会保存
f3 = shelve.open('shelve_file')
print(f3['key'])
f3['key']['new_value'] = 'this was not here before'
f3.close()

# writeback方式有优点也有缺点
# 优点是减少了我们出错的概率，并且让对象的持久化对用户更加的透明了；但这种方式并不是所有的情况下都需要
# 首先，使用writeback以后，shelve在open()的时候会增加额外的内存消耗，并且当db在close()的时候会将缓存中的每一个对象都写入到db，这也会带来额外的等待时间
# shelve没有办法知道缓存中哪些对象修改了，哪些对象没有修改，因此所有的对象都会被写入

f4 = shelve.open('shelve_file', writeback=True)
print(f4['key'])
f4['key']['new_value'] = 'this was not here before'
f4.close()
