"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p_423_3 file
Author: zhangxiaoan 00565442
Create: 2021/5/6 19:55
"""

def p3(s):
    n = len(s)
    maxlen = 0
    nums_cnts = [0 for _ in range(10)]
    num_counts = [[0 for _ in range(10)]]
    max_i, max_j, max_len = -1, -1, 0

    for i in range(n):
        c = ord(s[i]) - ord('0')
        nums_cnts[c] += 1
        num_counts.append(nums_cnts[:])

    def check_ok(i, j, num_counts):
        k = 0
        for num in range(10):
            if num_counts[j][num] - num_counts[i][num] == 1:
                k += 1
        return k == 2

    for i in range(n):
        start = min(n-1, i + max_len-1)
        for j in range(start, n):
            if check_ok(i, j+1, num_counts) and j - i + 1 > max_len:
                max_i, max_j, max_len = i, j, j - i + 1

    return s[max_i:max_j+1]

if __name__ == "__main__":
    print(p3("02280609665"))

