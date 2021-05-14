"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p02 file
Author: zhangxiaoan 00565442
Create: 2021/5/12 9:44
"""

def insert_str(score, digit):
    if digit[0] == '0':
        max_str = score[0] + digit + score[1:]
        first_pos = 2
    else:
        max_str = digit + score
        first_pos = 1

    for pos in range(first_pos, n+1):
        sub_str =