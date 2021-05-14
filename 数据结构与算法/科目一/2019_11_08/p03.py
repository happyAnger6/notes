"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p03 file
Author: zhangxiaoan 00565442
Create: 2021/5/12 21:45
"""
from collections import defaultdict
def can_finish(num_courses, pre_requires):
    n = num_courses
    adjs = defaultdict(list)
    in_degrees = [0 for _ in range(n)]
    visited = [0 for _ in range(n)]
    valid = True

    for start, end in pre_requires:
        adjs[start].append(end)
        in_degrees[end] += 1

    def dfs(start):
        nonlocal adjs, visited, valid

        if visited[start] != 0:
            valid = False
            return

        visited[start] = 1
        for adj in adjs[start]:
            if visited[adj] == 1:
                valid = False
                return

            if visited[adj] == 0:
                dfs(adj)
                if not valid:
                    return
        visited[start] = 2
        return True

    for i, degree in enumerate(in_degrees):
        if valid and visited[i] == 0:
            dfs(i)

    return valid

if __name__ == "__main__":
    print(can_finish(2, [[1, 0]]))
    print(can_finish(2, [[1, 0], [0, 1]]))
    print(can_finish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
    print(can_finish(5, [[1,4],[2,4],[3,1],[3,2]]))
