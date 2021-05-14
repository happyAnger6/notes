"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p560 file
Author: zhangxiaoan 00565442
Create: 2021/5/10 20:13
"""
def subarray_num(nums, k):
    n = len(nums)
    prefix_sums = [0 for _ in range(n)]
    cur_sum = 0
    for i, num in enumerate(nums):
        cur_sum += num
        prefix_sums[i] = cur_sum

    total = 0
    def merge_sort(nums, i, j, k):
        nonlocal total, prefix_sums
        if i > j:
            return

        if i == j:
            if prefix_sums[i] == k:
                total+=1
            return

        mid = i + (j - i)//2
        merge_sort(nums, i, mid, k)
        merge_sort(nums, mid+1, j, k)
        left, right = i, mid+1
        left_num = 0
        while left <= mid and right <= j:
            cur_sum = prefix_sums[right] - prefix_sums[left]
            if cur_sum == k:
                total += 1
                left_num += 1
                right += 1
                if right > j:
                    left += 1
                    while left <= mid and prefix_sums[left] == prefix_sums[left-1]:
                        total += left_num
                        left += 1
                    break
            elif cur_sum > k:
                left += 1
                while left <= mid and prefix_sums[left] == prefix_sums[left - 1]:
                    total += left_num
                    left += 1
                left_num = 0
            else:
                right += 1

        new_prefix_nums = []
        left, right = i, mid + 1
        while left <= mid and right <= j:
            if prefix_sums[left] <= prefix_sums[right]:
                new_prefix_nums.append(prefix_sums[left])
                left += 1
            else:
                new_prefix_nums.append(prefix_sums[right])
                right += 1

        if left <= mid:
            new_prefix_nums.extend(prefix_sums[left:mid+1])
        if right <= j:
            new_prefix_nums.extend(prefix_sums[right:j+1])
        prefix_sums[i:j+1] = new_prefix_nums[:]

    merge_sort(nums, 0, n-1, k)
    return total


if __name__ == "__main__":
    print(subarray_num([1, 1, 1], 2))
    print(subarray_num([1, 1, 0, 0, 1], 2))
    print(subarray_num([1], 0))
    print(subarray_num([1, 2, 3], 3))
    print(subarray_num([-1, -1, 1], 0))
    print(subarray_num([1, 3, 2, 0, 3, 3], 3))
    print(subarray_num([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0))
