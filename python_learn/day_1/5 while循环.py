# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 19:56
# @python  : python 3.7
# @Author  : 水萍
# @File    : 5 while循环.py
# @Software: PyCharm

# 死循环
# while True:
# 	print("我们不一样")
# 	print("月亮之上")
# 	print("人间")

# 1~100所有数字
count = 0
flag = True
while flag:
	count += 1
	print(count)
	if count == 100:
		flag = False

while count < 100:
	count += 1
	print(count)

# 1+2+3+...99的结果
sum = 0
count = 1
while count < 100:
	sum += count
	print("%d+" %count, end='')
	if count == 99:
		print("%d=" % count, end='')
	count += 1
print(sum)

# continue退出本次循环
flag = True
while flag:
	print(111)
	print(222)
	flag = False
	continue
	print(333)

# whlie...else:while循环被break打断，则不执行else语句
count = 1
while count < 5:
	print(count)
	# if count == 2:
	# 	break
	count += 1
else:
	print(666)

# 猜大小
num = 17
count = 0
while count < 3:
	tmp = input("请输入你猜的数字：")
	if int(tmp) == num:
		print("猜对了，你真聪明！")
		break
	elif int(tmp) > num:
		print("太大了！")
	else:
		print("太小了！")
	count += 1
else:
	print("太笨了！")


# 1-2+3-4+5...99的和
sum=0
count = 1
while count < 100:
	if count == 99:
		print("%d=" % count, end='')
		sum += count
	else:
		if count %2 == 1:
			sum += count
			print("%d-" % count, end='')
		else:
			sum -= count
			print("%d+" % count, end='')

	count += 1
print(sum)