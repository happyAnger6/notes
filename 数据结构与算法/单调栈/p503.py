"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p503 file
Author: zhangxiaoan 00565442
Create: 2021/5/10 18:51
"""

def next_greater_elemnts(nums):
    n = len(nums)
    results = [-1 for _ in range(n)]
    stack = []
    i = 0
    while i < 2 * n:
        j = i % n
        num = nums[j]
        while stack and num > nums[stack[-1]]:
            pos = stack.pop()
            if results[pos] == -1:
                results[pos] = num
        stack.append(j)
        i += 1
    return results

if __name__ == "__main__":
    print(next_greater_elemnts([1, 2, 1]))
