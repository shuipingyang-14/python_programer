set1 =set({1, 3, 3, 2, False, 'hello'})
print(set1)

set2 = set()
print(type(set2))

# 集合内元素不可变
# set3 = {[1,2], 2, {"name":"hello"}}
# print(set3)

# 1.增加元素
set1 = {'太白', 'hello', '小红', 'alex', '1', 2}
print(set1)
set1.add('xx')
print(set1)
set1.update('sfgdgwu')
print(set1)

# 2.删除元素
set1.remove('alex')
print(set1)
set1.pop()  # 随机删除
print(set1)

# 3.交集
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
print(set1 & set2)

# 4.并集
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
print(set1 | set2)

# 5. 差集
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
print(set1 - set2)
print(set2 - set1)

# 6.反交集
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
print(set1 ^ set2)

# 7.子集
set1 = {1,2,3}
set2 = {1,2,3,4,5,6}
print(set1 < set2)

# 8.超子集
set1 = {1,2,3}
set2 = {1,2,3,4,5,6}
print(set2 > set1)