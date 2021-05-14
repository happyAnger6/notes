"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p1723 file
Author: zhangxiaoan 00565442
Create: 2021/5/7 9:43
"""
import heapq

def minimum_time_required(jobs, k):
    min_max = float("inf")
    def all_subsets(jobs, k, subset=None):
        if subset is None:
            subset = []



if __name__ == "__main__":
    print(minimum_time_required([3, 2, 3], 3))
    print(minimum_time_required([1, 2, 4, 7, 8], 2))
