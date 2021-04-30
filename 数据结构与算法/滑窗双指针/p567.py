"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p567 file
Author: zhangxiaoan 00565442
Create: 2021/4/27 9:04

Q: p567.字符串的排列(https://leetcode-cn.com/problems/permutation-in-string/)
"""
from collections import defaultdict
def checkInclusion(s1, s2):
    n1, n2 = len(s1), len(s2)
    if n2 < n1:
        return False

    char_cnts = defaultdict(int)
    diff_chars = 0
    for i, char in enumerate(s1):
        char_cnts[char] += 1
        if char_cnts[char] == 1:
            diff_chars += 1

    chars = 0
    for right, char in enumerate(s2):
        if right >= n1:
            left_char = s2[right - n1]
            if left_char in char_cnts:
                char_cnts[left_char] += 1
                if char_cnts[left_char] == 1:
                    chars -= 1

        if char in char_cnts:
            char_cnts[char] -= 1
            if char_cnts[char] == 0:
                chars += 1

        if chars == diff_chars:
            return True

    return False

if __name__ == "__main__":
    print(checkInclusion("ab", "eidbaooo"))
    print(checkInclusion("ab", "eidboaoo"))
    print(checkInclusion("trinitrophenylmethylnitramine", "nitrophenylhydrazinetrinitrophenylmethylnitramine"))





