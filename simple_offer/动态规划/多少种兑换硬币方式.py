# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/24 10:57
@ file:     多少种兑换硬币方式.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# 给定不同面额的硬币和一个总金额，写出函数来计算可以凑成总金额的硬币组合数，假设每一种面额的硬币有无限个
def ways_to_change(n):
    mod = 10**9+7

    coins = [1,2,5]

    f = [1] + [0]*n

    for coin in coins:
        for i in range(coin, n+1):
            f[i] += f[i-coin]
    print(f)

    return f[n]%mod

def ways_to_change_1(n):

    coins = [1, 2, 5]

    dp = [0]*(n+1)
    dp[0] = 1

    for coin in coins:
        for x in range(coin, n+1):
            dp[x] = (dp[x] + dp[x-coin])
    print(dp)

    return dp[n]

if __name__ == '__main__':
    print(ways_to_change(2))
    print(ways_to_change_1(11))