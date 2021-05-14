"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p01 file
Author: zhangxiaoan 00565442
Create: 2021/5/12 19:52
"""

def next_greater_elements(nums):
    n = len(nums)
    res = [-1 for _ in range(n)]

    stack = [(n-1, nums[-1])]
    i = n - 2
    while i >= 0:
        num = nums[i]
        while stack and num < stack[-1][1]:
            j, _ = stack.pop()
            res[j] = nums[i]
        stack.append((i, num))
        i -= 1
    return res

if __name__ == "__main__":
    print(next_greater_elements([1, 6, 4, 10, 2, 5]))
    print(next_greater_elements([2, 4, 1, 3, 6]))

