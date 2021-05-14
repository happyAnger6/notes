"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p128 file
Author: zhangxiaoan 00565442
Create: 2021/5/8 9:09
"""
def longest_consecutive(nums):
    if not nums:
        return 0

    s_nums = sorted(nums)
    max_len, cur_len = 0, 1
    for i, num in enumerate(s_nums):
        if i > 0:
            if num == s_nums[i-1] + 1:
                cur_len += 1
            elif num != s_nums[i-1]:
                cur_len = 1
        max_len = max(max_len, cur_len)
    return max_len

if __name__ == "__main__":
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))
    print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))
    print(longest_consecutive([0,2,1,2,2]))



