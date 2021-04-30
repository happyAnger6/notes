"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p_array_sum file
Author: zhangxiaoan 00565442
Create: 2021/4/30 15:57
"""

def array_sum(nums):
    def sum_array(nums, i, j):
        if j < i:
            return 0

        if i == j:
            return nums[i]

        mid = i + (j - j) // 2
        left_sum = sum_array(nums, i, mid)
        right_sum = sum_array(nums, mid+1, j)
        return left_sum + right_sum
    return sum_array(nums, 0, len(nums)-1)

if __name__ == "__main__":
    print(array_sum([1, 3, 5, 7, 9]))
    print(array_sum([]))
    print(array_sum([0]))
