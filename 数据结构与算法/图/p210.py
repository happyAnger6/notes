"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p210 file
Author: zhangxiaoan 00565442
Create: 2021/5/14 9:15
"""
from collections import defaultdict
def find_order(num_courses, pre_requires):
    ret = []
    n = num_courses
    visited = defaultdict(int)
    valid = True

    adjs = defaultdict(list)
    for pre_require in pre_requires:
        start, end = pre_require
        adjs[start].append(end)

    def dfs(i):
        nonlocal visited, adjs, ret, valid

        visited[i] = 1
        for adj in adjs[i]:
            if visited[adj] == 1:
                valid = False
                return

            if visited[adj] == 2:
                continue

            dfs(adj)
            if not valid:
                return

        visited[i] = 2
        ret.append(i)

    for i in range(n):
        if valid and visited[i] == 0:
            dfs(i)

    if valid:
        return ret

    return []

if __name__ == "__main__":
    nums = 2
    pre_requires = [[1, 0]]
    print(find_order(nums, pre_requires))
    nums = 4
    pre_requires = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(find_order(nums, pre_requires))

