"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p253 file
Author: zhangxiaoan 00565442
Create: 2021/5/12 21:37
"""
import heapq
def min_meeting_rooms(intervals):
    hq = []
    s_intervals = sorted(intervals, key=lambda x:x[0])
    heapq.heappush(hq, s_intervals[0][1])
    for start, end in s_intervals[1:]:
        if start >= hq[0]:
            heapq.heappop(hq)
        heapq.heappush(hq, end)
    return len(hq)

if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(min_meeting_rooms(intervals))
    intervals = [[7, 10], [2, 4]]
    print(min_meeting_rooms(intervals))


