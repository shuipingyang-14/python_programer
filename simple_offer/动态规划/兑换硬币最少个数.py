# -*- coding:utf-8
"""
@ author:   ysp
@ time：    2020/6/24 11:43
@ file:     兑换硬币最少个数.py
@ IDE:      PyCharm
@ version:  python 3.8.3
"""

# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1

def coin_change(coins, amount):
    dp = [float('inf')]*(amount+1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount+1):
            dp[x] = min(dp[x], dp[x-coin]+1)
    print(dp)
    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == '__main__':
    coins = [1,2,5]
    print(coin_change(coins, 3))
    print(coin_change(coins, 6))
    print(coin_change(coins, 11))
