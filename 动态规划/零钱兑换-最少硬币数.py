# -*- coding: utf-8

# @Author    : shiwl
# @Time      : 2022/10/9 下午3:04
# @File      : 零钱兑换
import math

res = math.inf
# 树型DP（递归）
def func1(coins, total):
    if not coins or len(coins) == 0:
        return -1

    find1(coins, total, 0)

    if res == math.inf:
        return -1

    return res


def find1(coins, total, count):
    # base case
    if total < 0:
        return -1

    if total == 0:
        global res
        res = min(res, count)

    for i in range(0, len(coins)):
        count += 1
        find1(coins, total - coins[i], count)

memory_dp = []
# 记忆化搜索
def func2(coins, total):
    if not coins or len(coins) == 0:
        return -1

    return find2(coins, total)

def find2(coins, total):
    if total < 0:
        return -1

    if total == 0:
        return 0

    if memory_dp[total - 1]:
        return memory_dp[total - 1]

    mins = math.inf

    for i in range(0, len(coins)):
        res = find2(coins, total - coins[i])
        if res > 0 and res < mins:
            mins = res + 1

    memory_dp[total - 1] = -1 if mins == math.inf else mins

    return memory_dp[total - 1]


# 动态规划
def func3(coins, total):
    if not coins or len(coins) == 0:
        return -1

    dp = []
    dp[0] = 0

    for i in range(1, total):
        mins = math.inf
        for j in range(0, len(coins)):
            if i - coins[j] >=0 and dp[i-coins[j]] <= mins:
                mins = dp[i-coins[j]] + 1
        dp[i] = mins
    return -1 if dp[total] == math.inf else dp[total]

