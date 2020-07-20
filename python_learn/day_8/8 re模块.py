# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/4 15:05
@ file:     8 re模块.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# 正则使用一些具有特殊含义的符号组合到一起（称为正则表达式）来描述字符或者字符串的方法

# 字符串匹配
s1 = 'helloworld你好世界'
print(s1.find('你好'))   # 10

# 1.正则匹配
# 单个字符匹配
import re
# \w       匹配字母（包含中文）或数字或下划线
print(re.findall('\w', 'hello你好 12*() _'))
# ['h', 'e', 'l', 'l', 'o', '你', '好', '1', '2', '_']

# \W       匹配非字母（包含中文）或数字或下划线
print(re.findall('\W', 'hello你好 12*() _'))
# [' ', '*', '(', ')', ' ']

# \s       匹配任意空白符
print(re.findall('\s', '太白barry*(_ \t \n'))
# [' ', '\t', ' ', '\n']

# \S       匹配任意非空白符
print(re.findall('\S', '太白barry*(_ \t \n'))
# ['太', '白', 'b', 'a', 'r', 'r', 'y', '*', '(', '_']

# \d       匹配数字
print(re.findall('\d', '1234567890 alex *（_'))
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# \D       匹配非数字
print(re.findall('\D', '1234567890 alex *（_'))
# [' ', 'a', 'l', 'e', 'x', ' ', '*', '（', '_']

# \A       从字符串开头匹配
print(re.findall('\A', 'hello 太白金星 -_- 666'))
# [' ']

# ^        匹配字符串开始
print(re.findall('^hel','hello 太白金星 -_- 666'))
# ['hel']

# \z       匹配字符串结束，如果是换行，只匹配到换行前的结果
print(re.findall('666\Z','hello 太白金星 *-_-* \n666'))
# ['666']

# $        匹配子字符串结尾
print(re.findall('666$','hello 太白金星 *-_-* \n666'))
# ['666']

# \n       匹配一个换行符
print(re.findall('\n','hello \n 太白金星 \t*-_-*\t \n666'))
# ['\n', '\n']

# \t       匹配一个制表符
print(re.findall('\t','hello \n 太白金星 \t*-_-*\t \n666'))
# ['\t', '\t']

# 重复匹配 . ? * + {m,n} .* .*?
# .        匹配任意字符，除了换行符，当re.DOTALL标记被指定时，可以匹配包括换行符的任意字符
print(re.findall('a.b', 'ab aab a*b axb a\nb'))
# ['aab', 'a*b' ,'axb']
print(re.findall('a.b', 'ab aab a*b axb a\nb', re.DOTALL))
# ['aab', 'a*b', 'axb', 'a\nb']
print(re.findall('a.b', 'a1b a3b aeb a*b arb a_b'))
# ['a1b', 'a3b', 'a4b', 'a*b', 'arb', 'a_b']

# ?        匹配0个或者一个左边字符，非贪婪方式
print(re.findall('a?b', 'ab aab abb aaaab a牛b aba**b'))
# ['ab', 'ab', 'ab', 'b', 'ab', 'b', 'ab', 'b']

# *        匹配0个或多个左边字符，贪婪匹配
print(re.findall('a*b', 'ab aab aaab abbb'))
# ['ab', 'aab', 'aaab', 'ab', 'b', 'b']
print(re.findall('ab*', 'ab aab aaab abbbbb'))
# ['ab', 'a', 'ab', 'a', 'a', 'ab', 'abbbbb']

# +        匹配一个或者多个左边字符，贪婪匹配
print(re.findall('a+b', 'ab aab aaab abbb'))
# ['ab', 'aab', 'aaab', 'ab']

# {m,n}  匹配m个至n个左边字符表达式，贪婪匹配
print(re.findall('a{2,4}b', 'ab aab aaab aaaaabb'))
# ['aab', 'aaab', 'aaaab']

# .* 贪婪匹配 从头到尾.
print(re.findall('a.*b', 'ab aab a*()b'))
# ['ab aab a*()b']

# .*? 此时的?不是对左边的字符进行0次或者1次的匹配,
# 而只是针对.*这种贪婪匹配的模式进行一种限定:告知他要遵从非贪婪匹配 推荐使用!
print(re.findall('a.*?b', 'ab a1b a*()b, aaaaaab'))
# ['ab', 'a1b', 'a*()b', 'aaaaaab']

# []  括号中可以放任意一个字符，一个中括号代表一个字符
# - 在[]中表示范围，如果相匹配-那么-不可在中间
# ^ 在[]中表示取反
print(re.findall('a[abc]b', 'aab abb acb adb afb a_b'))
# ['aab', 'abb', 'acb']
print(re.findall('a[0-9]b', 'a1b a3b aeb a*b arb a_b'))
# ['a1b', 'a3b']
print(re.findall('a[a-z]b', 'a1b a3b aeb a*b arb a_b'))
# ['aeb', 'arb']
print(re.findall('a[a-zA-Z]b', 'aAb aWb aeb a*b arb a_b'))
# ['aAb', 'aWb', 'aeb', 'arb']
print(re.findall('a[0-9][0-9]b', 'a11b a12b a34b a*b arb a_b'))
# ['a11b', 'a12b', 'a34b']
print(re.findall('a[*-+]b','a-b a*b a+b a/b a6b'))
# ['a*b', 'a+b']
print(re.findall('a[-*+]b','a-b a*b a+b a/b a6b'))
# ['a-b', 'a*b', 'a+b']
print(re.findall('a[^a-z]b', 'acb adb a3b a*b'))
# ['a3b', 'a*b']

# () 制定一个规则,将满足规则的结果匹配出来
print(re.findall('(.*?)_sb', 'alex_sb wusir_sb 日天_sb'))
# ['alex', ' wusir', ' 日天']
print(re.findall('href="(.*?)"','<a href="http://www.baidu.com">点击</a>'))
# ['http://www.baidu.com']

# | 匹配 左边或者右边
print(re.findall('alex|太白|wusir', 'alex太白wusiraleeeex太太白odlb'))
# ['alex', '太白', 'wusir', '太白']
print(re.findall('compan(y|ies)','Too many companies have gone bankrupt, and the next one is my company'))
# ['ies', 'y']
print(re.findall('compan(?:y|ies)','Too many companies have gone bankrupt, and the next one is my company'))
# ['companies', 'company']
# 分组() 中加入?: 表示将整体匹配出来而不只是()里面的内容

# 2.常用方法
# findall 全部找到返回一个列表
print(re.findall('a', 'alexwusirgarryeval'))
# ['a', 'a', 'a']
print(re.findall('sb|alex', 'alex sb sb barry 你好'))
# ['alex', 'sb', 'sb']

# search 只找到第一个匹配然后返回一个包含匹配信息的对象，该对象可以通过调用group()方法得到匹配的字符串，如果字符没有匹配，返回None
print(re.search('sb|alex', 'alex sb sb barry 你好'))
# <re.Match object; span=(0, 4), match='alex'>
print(re.search('alex', 'alex sb sb barry 你好').group())
# alex

# match：None,同search,不过在字符串开始处进行匹配,完全可以用search+^代替match
print(re.match('barry', 'barry alex wusir 日天'))
# <re.Match object; span=(0, 5), match='barry'>
print(re.match('barry', 'barry alex wusir 日天').group())
# barry

# spilt 分割，按照任意分割符进行分割
print(re.split('[ ：:,;；，]','alex wusir,日天，太白;女神;肖锋：吴超'))
# ['alex', 'wusir', '日天', '太白', '女神', '肖锋', '吴超']

# sub 替换
print(re.sub('barry', 'alex', 'barry是好的老师，barry就是一个普通老师，请不要将barry当男神对待'))
# alex是好的老师，alex就是一个普通老师，请不要将alex当男神对待
print(re.sub('barry', 'alex', 'barry是好的老师，barry就是一个普通老师，请不要将barry当男神对待', 2))
# alex是好的老师，alex就是一个普通老师，请不要将barry当男神对待
print(re.sub('([a-zA-Z]+)([^a-zA-Z]+)([a-zA-Z]+)([^a-zA-Z]+)([a-zA-Z]+)', r'\5\4\3\2\1', r'alex is sb'))
# sb is alex

# compile
obj = re.compile('\d[2]')

print(obj.search('abc123eeee').group())  # 12
print(obj.findall('abc123eeee'))   # ['12']

# finditer 返回一个存放匹配结果的迭代器
ret = re.finditer('\d', 'ds3sy784a')
print(ret)  # <callable_iterator object at 0x010752B0>
print(next(ret).group())  #查看第一个结果 3
print(next(ret).group())  #查看第二个结果 7
print([i.group() for i in ret])  #查看剩余的结果  # ['8', '4']

# 命名分组匹配
ret = re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>")
print(ret.group())  # <h1>hello</h1>
# 在分组中利用?<name>形式给分组起名字
print(ret.group('tag_name'))  # h1
# 获取的匹配结果可以直接用group('name')拿到对应值

ret = re.search(r"<(\w+)>\w+</\1>", "<h1>hello</h1>")
# 如果不起名字，可以用\序号来找到对应组，表示要找的内容和前面的组内容一致
# 获取的匹配结果可以直接用group(序号)拿到对应值
print(ret.group())  # <h1>hello</h1>
print(ret.group(1))  # h1

s = "1-2*(60+(-40.35/5)-(-4*3))"
# 匹配所有整数
print(re.findall('\d+', s))
# ['1', '2', '60', '40', '35', '5', '4', '3']
# 匹配所有数字（包含小数）
print(re.findall(r'\d+\.?\d*|\d*\.?\d+', s))
# ['1', '2', '60', '40.35', '5', '4', '3']
# 匹配所有数字（包含小数和负号）
print(re.findall(r'-?\d+\.?\d*|\d*\.?\d+', s))

# 匹配一段文本中时间字符串
s1 = '''
时间就是1995-04-27,2005-04-27
1999-04-27 老男孩教育创始人
老男孩老师 alex 1980-04-27:1980-04-27
2018-12-08
'''
print(re.findall('\d{4}-\d{2}-\d{2}', s1))
# ['1995-04-27', '2005-04-27', '1999-04-27', '1980-04-27', '1980-04-27', '2018-12-08']
