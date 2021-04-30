"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p215 file
Author: zhangxiaoan 00565442
Create: 2021/4/30 16:19
"""

def top_k(nums, k):
    def partition(nums, left, right):
        if left >= right:
            return 1

        sel = nums[right]
        pos = left-1
        start = left
        while start < right:
            if nums[start] > sel:
                pos += 1
                if start != pos:
                    tmp = nums[pos]
                    nums[pos] = nums[start]
                    nums[start] = tmp
            start += 1
        pos += 1
        nums[pos], nums[right] = sel, nums[pos]
        return pos - left + 1

    def quick_find(nums, left, right, k):
        m = partition(nums, left, right)
        if m == k:
            return nums[left + m - 1]

        if m > k:
            return quick_find(nums, left, left + m - 2, k)
        else:
            return quick_find(nums, left + m, right, k - m)
    return quick_find(nums, 0, len(nums)-1, k)

if __name__ == "__main__":
    print(top_k([1], 1))
    print(top_k([3, 1, 2, 4], 2))
    print(top_k([3, 2, 1, 5, 6, 4], 2))
    print(top_k([5, 2, 4, 1, 3, 6, 0], 4))
