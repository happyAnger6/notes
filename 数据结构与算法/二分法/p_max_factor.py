"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p_max_factor file
Author: zhangxiaoan 00565442
Create: 2021/4/30 16:01
"""

def max_factor(m, n):
    while m % n != 0:
        tmp = n
        n = m % n
        m = tmp
    return n

if __name__ == "__main__":
    print(max_factor(15, 9))
    print(max_factor(24, 18))
