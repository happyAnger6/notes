"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p343 file
Author: zhangxiaoan 00565442
Create: 2021/5/7 21:05
"""

def integer_break(n):
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    for i in range(2, n+1):
        for j in range(1, i//2+1):
            dp[i] = max(dp[i], max(dp[j], j) * max(i-j,dp[i-j]))
    return dp[n]

if __name__ == "__main__":
    print(integer_break(2))
    print(integer_break(10))

