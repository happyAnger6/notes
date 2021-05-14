"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p209 file
Author: zhangxiaoan 00565442
Create: 2021/5/10 19:42
"""

def min_sub_array(s, nums):
    cur_sum, n = 0, len(nums)
    left, right = 0, 0
    min_len = float("inf")
    while right < n:
        cur_sum += nums[right]
        while cur_sum >= s:
            min_len = min(min_len, right - left + 1)
            cur_sum -= nums[left]
            left += 1
        right += 1

    return min_len if min_len != float("inf") else 0

if __name__ == "__main__":
    print(min_sub_array(7, [2, 3, 1, 2, 4, 3]))
    print(min_sub_array(4, [1, 4, 4]))
    print(min_sub_array(11, [1, 1, 1, 1, 1, 1, 1, 1]))
