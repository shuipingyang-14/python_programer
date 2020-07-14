# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/7/13 10:31
@ file:     4 面向对象-类关系.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# 类与类之间的关系：
# 1. 依赖关系
class Elphant:
    def __init__(self, name):
        self.name = name

    def open(self, obj):
        """开门"""
        print('大象要开门了，默念三声，开')
        obj.open_door()

    def close(self):
        """关门"""
        print('大象要关门了，默念三声，关')


class Refrigerator:

    def open_door(self):
        print("冰箱被打开了")

    def close_door(self):
        print("冰箱被关上了")

elp = Elphant('大象')
haler = Refrigerator()
elp.open(haler)

# 2. 关联关系：两种事物必须是互相关联的，但是在某些特殊情况下是可以更改和更换的
class Boy:
    def __init__(self, name, girlFriend = None):
        self.name = name
        self.girlFriend = girlFriend

    def have_a_diner(self):
        if self.girlFriend:
            print('%s 和 %s 一起晚饭' % (self.name, self.girlFriend.name))
        else:
            print('单身狗，吃什么饭')

class Girl:
    def __init__(self, name):
        self.name = name

# 单身狗
b = Boy('alex')
b.have_a_diner()

# 交了女朋友
b.girlFriend = Girl('jefrry')
b.have_a_diner()

# wusir 生下来就有女朋友 服不服
gg = Girl('小花')
bb = Boy('wusir', gg)
bb.have_a_diner()

#分手了
bb.girlFriend = None
bb.have_a_diner()


# 老师属于学校，必须有学校才可以工作
class School:

    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.teacher_list = []

    def append_teacher(self, teacher):
        self.teacher_list.append(teacher)

class Teacher:

    def __init__(self,name,school):
        self.name = name
        self.school = school

s1 = School('北京校区','美丽的沙河')
s2 = School('上海校区','上海迪士尼旁边')
s3 = School('深圳校区','南山区')

t1 = Teacher('武大',s1)
t2 = Teacher('海峰',s2)
t3 = Teacher('日天',s3)

s1.append_teacher(t1)
s1.append_teacher(t2)
s1.append_teacher(t3)

print(s1.teacher_list)
for teacher in s1.teacher_list:
    print(teacher.name)

# 3. 组合关系：属于关联关系中的⼀种特例，侧重点是xxx和xxx聚合成xxx. 各⾃有各⾃的声明周期

class Gamerole:
    def __init__(self, name, ad, hp):
        self.name = name
        self.ad = ad
        self.hp = hp

    def attack(self, p1):
        p1.hp -= self.ad
        print('%s攻击%s,%s掉了%s血,还剩%s血' % (self.name, p1.name, p1.name, self.ad, p1.hp))

    def equip_weapon(self, wea):
        self.wea = wea  # 组合：给一个对象封装一个属性改属性是另一个类的对象


class Weapon:
    def __init__(self, name, ad):
        self.name = name
        self.ad = ad

    def weapon_attack(self, p1, p2):
        p2.hp = p2.hp - self.ad - p1.ad
        print('%s 利用 %s 攻击了%s,%s还剩%s血'
              % (p1.name, self.name, p2.name, p2.name, p2.hp))


# 实例化三个人物对象：
barry = Gamerole('太白', 10, 200)
panky = Gamerole('金莲', 20, 50)
pillow = Weapon('绣花枕头', 2)

# 给人物装备武器对象。
barry.equip_weapon(pillow)

# 开始攻击
barry.wea.weapon_attack(barry, panky)
