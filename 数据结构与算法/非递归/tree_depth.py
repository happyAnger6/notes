"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut tree_depth file
Author: zhangxiaoan 00565442
Create: 2021/5/13 19:03
"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_depth(root):
    stack = []
    max_height = 0
    node, height = root, 1
    while stack or node:
        if node:
            stack.append((node, height))
            max_height = max(max_height, height)
            node = node.left
        else:
            node, height = stack.pop()
            node = node.right
        height += 1
    return max_height

if __name__ == "__main__":
    root = Node(1, Node(2, None, Node(3)), Node(4, Node(5, None, Node(7)), Node(6)))
    print(tree_depth(root))
