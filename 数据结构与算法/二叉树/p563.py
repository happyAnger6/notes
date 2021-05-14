"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p563.py file
Author: zhangxiaoan 00565442
Create: 2021/5/7 20:54
"""

def findTilt(root):
    tilt = 0
    def post_traverse(root):
        nonlocal tilt
        if root is None:
            return 0

        left_sum = post_traverse(root.left)
        right_sum = post_traverse(root.right)
        tilt += abs(left_sum - right_sum)
        return left_sum + right_sum + root.val

    post_traverse(root)
    return tilt
