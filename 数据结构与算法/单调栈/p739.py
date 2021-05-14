"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p739 file
Author: zhangxiaoan 00565442
Create: 2021/5/10 19:02
"""

def daily_temperatures(T):
    n = len(T)
    results = [0 for _ in range(n)]

    stack = []
    for i, t in enumerate(T):
        while stack and t > stack[-1][0]:
            e, j = stack.pop()
            results[j] = i - j
        stack.append((t, i))
    return results

if __name__ == "__main__":
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))