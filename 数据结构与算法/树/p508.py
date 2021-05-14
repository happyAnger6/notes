"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p508 file
Author: zhangxiaoan 00565442
Create: 2021/5/12 19:04
"""
from collections import defaultdict


def find_freq_tree_sum(root):
    total_maps = defaultdict(int)
    def post_traverse(node):
        nonlocal total_maps
        if node is None:
            return 0

        left = post_traverse(node.left)
        right = post_traverse(node.right)
        total_maps[node.val + left + right] += 1

    post_traverse(root)

    s_t = sorted(total_maps.items(), key=lambda x: x[1], reverse=True)
    num, times = s_t[0]
    res = [num]
    for i, v in s_t:
        if v != times:
            break
        res.append(i)
    return res

