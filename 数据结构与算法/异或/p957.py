"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p957 file
Author: zhangxiaoan 00565442
Create: 2021/5/13 19:26
"""

def prison_after_nDays(cells, n):
    prev_cells = cells
    next_cells = cells[:]
    while n > 0:
        n -= 1
        next_cells[0] = next_cells[-1] = 0
        for i in range(1, 7):
            next_cells[i] = prev_cells[i-1]^prev_cells[i+1]^1
        prev_cells = next_cells
        next_cells = prev_cells[:]
    return next_cells

if __name__ == "__main__":
    print(prison_after_nDays([0, 1, 0, 1, 1, 0, 0, 1], 7))


