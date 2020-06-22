# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/28 10:26
@ file:     生成器-推导式构建.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""
# 1. 列表推导式分为两种模式：
# 循环模式：[变量(加工的变量) for 变量 in iterable]

# a. 列表中添加1~10
l1 = []
for i in range(1, 11):
    l1.append(i)

print(l1)

l2 = [i for i in range(1, 11)]
print(l2)

# b. 将10以内整数平方写入列表
l3 = [x * x for x in range(1, 11)]
print(l3)

# c. 100以内所有偶数写入列表
l4 = [x for x in range(2, 101, 2)]
print(l4)

# 筛选模式: [变量(加工的变量) for 变量 in iterable if 条件]

# 取出列表中大于3的元素
l1 = [4, 3, 2, 5, 6, 4, 7, 8]
print([i for i in l1 if i > 3])

# 三十以内能被三整除的数
print([i for i in range(1, 30) if i % 3 == 0])

# 过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
l = ['wusir', 'laonanhai', 'aa', 'b', 'taibai']
print([s.upper() for s in l if len(s) >= 3])

# 找到嵌套列表中名字含有两个‘e’的所有名字
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
print([name for index in names for name in index if name.count('e') == 2])

# 2. 生成器表达式
# 将十以内所有数的平方放到一个生成器表达式中
gen = (i ** 2 for i in range(10))
print(gen)  # 结果: <generator object <genexpr> at 0x0000026046CAEBF8>
for num in gen:
    print(num)

# 筛选生成器
gen = (i for i in range(1, 100) if i % 3 == 0)
for num in gen:
    print(num)

# 3. 生成器和列表推导式的区别
# a. 列表推导式耗内存，所有数据一次性加载到内存，而生成器表达式遵循迭代器协议，逐个产生元素
# b. 得到的值不一样，列表推导式得到的是一个列表，生成器表达式获取的是一个生成器
# c. 列表推导式一目了然，生成器表达式只是一个内存地址

# 生成器的惰性机制: 生成器只有在访问的时候才取值

# 4. 字典推导式
l1 = ['jay', 'jj', 'meet']
l2 =  ['周杰伦','林俊杰','郭宝元']
dic = {l1[i]:l2[i] for i in range(len(l1))}
print(dic)

# 5.集合推导式：生成一个集合,集合的特点;无序,不重复 所以集合推导式自带去重功能
lst = [1,2,3,-1,-3,-7,9]
s = {abs(i) for i in lst}
print(s)

