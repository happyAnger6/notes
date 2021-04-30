"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p1658 file
Author: zhangxiaoan 00565442
Create: 2021/4/28 9:15
"""

def min_operations(nums, s):
    n = len(nums)
    min_oper = float("inf")
    left, right, sum = -1, n-1, 0
    while left+1 < n:
        num = nums[left+1]
        if sum + num > s:
            break
        sum += num
        left += 1

    if sum == s:
        min_oper = left + 1

    while right > left:
        num = nums[right]
        while left >= 0 and sum + num > s:
            sum -= nums[left]
            left -= 1

        if sum + num > s:
            break

        sum += num
        if sum == s:
            min_oper = min(min_oper, left + 1 + n - right)

        right -= 1

    if min_oper == float("inf"):
        return -1
    return min_oper

if __name__ == "__main__":
    print(min_operations([1, 1, 4, 2, 3], 5))
    print(min_operations([5, 6, 7, 8, 9], 4))
    print(min_operations([5, 6, 7, 2, 2], 4))
    print(min_operations([3, 2, 20, 1, 1, 3], 10))
    print(min_operations([1, 1], 3))











