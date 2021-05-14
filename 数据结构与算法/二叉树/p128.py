"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p128 file
Author: zhangxiaoan 00565442
Create: 2021/5/8 9:09
"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert_node(self, node):
        if node.val <= self.val:
            if self.left is None:
                self.left = node
            else:
                self.left.insert_node(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert_node(node)

def longest_consecutive(nums):
    if not nums:
        return 0

    Root = Node(nums[0])
    for num in nums[1:]:
        new_node = Node(num)
        Root.insert_node(new_node)

    max_len, cur_len, prev = 0, 0, None
    stack = []
    node = Root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if prev is not None:
                if node.val - prev == 1:
                    cur_len += 1
                    prev = node.val
                elif node.val != prev:
                    prev = node.val
                    cur_len = 1
            else:
                prev = node.val
                cur_len = 1
            node = node.right
            max_len = max(max_len, cur_len)
    return max_len

if __name__ == "__main__":
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))
    print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))
    print(longest_consecutive([0,2,1,2,2]))



