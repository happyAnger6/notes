"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p128 file
Author: zhangxiaoan 00565442
Create: 2021/5/8 9:50
"""

def longest_consecutive(nums):
    s_nums = set(nums)

    max_len = 0
    while s_nums:
        num = s_nums.pop()
        cur_len = 1
        prev, next = num - 1, num + 1
        while next in s_nums:
            cur_len += 1
            s_nums.remove(next)
            next += 1
        while prev in s_nums:
            cur_len += 1
            s_nums.remove(prev)
            prev -= 1
        max_len = max(max_len, cur_len)
    return max_len

if __name__ == "__main__":
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))

