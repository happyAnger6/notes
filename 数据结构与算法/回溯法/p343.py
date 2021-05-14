"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p343 file
Author: zhangxiaoan 00565442
Create: 2021/5/7 21:05
"""

def integer_break(n):
    max_val = 0
    def break_next(n, val=None):
        nonlocal max_val
        if n == 0:
            max_val = max(val, max_val)
            return

        end = n + 1

        if val is None:
            val = 1
            end = n

        for i in range(1, end):
            break_next(n-i, val*i)

    break_next(n)
    return max_val

if __name__ == "__main__":
    print(integer_break(2))
    print(integer_break(10))

