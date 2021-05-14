"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p_hw03 file
Author: zhangxiaoan 00565442
Create: 2021/5/8 9:42
"""

def find_time(times, target):
    s_times = sorted(times, key=lambda x: x[0])

    def bin_search()