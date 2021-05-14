"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p684 file
Author: zhangxiaoan 00565442
Create: 2021/5/10 19:15
"""
def find_redundant_connection(edges):
    n = len(edges)
    parent = [i for i in range(n+1)]

    def find(parent, index):
        while parent[index] != index:
            index = parent[index]
        return index

    def union(parent, index1, index2):
        parent[index1] = parent[index2]

    for edge in edges:
        start, end = edge
        index1 = find(parent, start)
        index2 = find(parent, end)
        if index1 != index2:
            union(parent, index1, index2)
        else:
            return edge
    return -1

if __name__ == "__main__":
    print(find_redundant_connection([[1, 2], [1, 3], [2, 3]]))
    print(find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))

