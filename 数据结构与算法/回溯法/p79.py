"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p79 file
Author: zhangxiaoan 00565442
Create: 2021/5/6 19:34
"""

def exist(board, word):
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    row, col = len(board), len(board[0])
    seen = set()
    def dfs_search(pos, word):
        nonlocal board, dirs, row, col, seen

        n = len(word)
        if n == 0:
            return True

        x, y = pos
        if board[x][y] != word[0]:
            return False

        if n == 1:
            return True

        for dir_ in dirs:
            dir_x, dir_y = dir_
            next_x, next_y = x + dir_x, y + dir_y
            if next_x < 0 or next_x >= row:
                continue

            if next_y < 0 or next_y >= col:
                continue

            if (next_x, next_y) in seen:
                continue

            if board[next_x][next_y] != word[1]:
                continue

            seen.add((next_x, next_y))
            if dfs_search((next_x, next_y), word[1:]):
                return True
            seen.remove((next_x, next_y))

        return False

    for i in range(row):
        for j in range(col):
            seen.add((i, j))
            if dfs_search((i, j), word):
                return True
            seen.remove((i, j))

    return False

if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    print(exist(board, "ABCCED"))
    print(exist(board, "SEE"))
    print(exist(board, "ABCB"))

