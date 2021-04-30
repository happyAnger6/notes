"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p_bin_search file
Author: zhangxiaoan 00565442
Create: 2021/4/30 15:54
"""

def bin_search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

if __name__ == "__main__":
    print(bin_search([1, 3, 4, 5, 8, 10, 17, 21], 8))
    print(bin_search([1, 3, 4, 5, 8, 10, 17, 21], 1))
    print(bin_search([1, 3, 4, 5, 8, 10, 17, 21], 21))
    print(bin_search([1, 3, 4, 5, 8, 10, 17, 21], -1))
    print(bin_search([1, 3, 4, 5, 8, 10, 17, 21], 22))
