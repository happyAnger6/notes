"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p560 file
Author: zhangxiaoan 00565442
Create: 2021/5/10 20:13
"""
from collections import defaultdict
def subarray_num(nums, k):
    prefix_sums = defaultdict(int)
    prefix_sums[0] = 1
    cur_prefix_sum = 0
    cnts = 0
    for i, num in enumerate(nums):
        cur_prefix_sum += num
        cnts += prefix_sums[cur_prefix_sum-k]
        prefix_sums[cur_prefix_sum] += 1
    return cnts


if __name__ == "__main__":
    print(subarray_num([1, 1, 1], 2))
    print(subarray_num([1, 1, 0, 0, 1], 2))
    print(subarray_num([1], 0))
    print(subarray_num([1, 2, 3], 3))
    print(subarray_num([-1, -1, 1], 0))
