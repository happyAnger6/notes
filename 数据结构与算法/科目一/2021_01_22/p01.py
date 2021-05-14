"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p01 file
Author: zhangxiaoan 00565442
Create: 2021/5/12 9:14
"""
from collections import defaultdict
def employee(nums, scores, preferences):
    m, n = len(nums), len(scores)
    m_left, n_left = m, n
    d_hash = defaultdict(list)
    for i, preference in enumerate(preferences):
        for p in preference:
            d_hash[p].append((i, scores[i]))

    people_flags = [0 for _ in range(n)]
    d_ok = [0 for _ in range(m)]

    for i, num in enumerate(nums):
        peoples = d_hash[i]
        s_peoples = sorted(peoples, key=lambda x: x[1], reverse=True)
        left = num
        if left == 0:
            m_left -= 1
            continue

        for j, score in s_peoples:
            if people_flags[j] == 1:
                continue
            people_flags[j] = 1
            n_left -= 1
            left -= 1
            if left == 0:
                d_ok[i] = 1
                m_left -= 1
                break
    return [m_left, n_left]


if __name__ == "__main__":
    print(employee([1, 2, 1], [67, 58, 89, 42, 27], [[0, 1], [1], [0, 2], [2], [0]]))
    print(employee([3, 2, 0], [67, 89, 67, 42], [[2, 1], [1], [1, 2], [1]]))
