"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p1723 file
Author: zhangxiaoan 00565442
Create: 2021/5/7 21:29
"""

def minimum_time_required(jobs, k):
    n = len(jobs)
    dp = [0 for _ in range(1<<n)]
    for i in range(1<<n):
        end = n - 1
        pos = i
        while i != 0:
            if i & 1 == 1:
                dp[pos] += jobs[end]
            i >>= 1
            end -= 1

    return dp

if __name__ == "__main__":
    print(minimum_time_required([3, 2, 3], 3))
