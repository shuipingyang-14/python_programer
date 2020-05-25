# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/5/22 22:30
@ file:     罗马数字.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

def intToRoman(num):
    # 贪心算法
    rule = (
        ('M', 1000),
        ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
        ('XC', 90), ('L', 50), ('XL', 40), ('X', 10),
        ('IX', 9), ('V', 5), ('IV', 4), ('I', 1),
    )
    result = ''

    for letter,number in rule:
        if num >= number:
            result += letter*(num//number)
            num %= number
    return result


if __name__ == '__main__':
    ret = intToRoman(999)
    print(ret)