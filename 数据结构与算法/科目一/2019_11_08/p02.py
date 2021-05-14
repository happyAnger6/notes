"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p02 file
Author: zhangxiaoan 00565442
Create: 2021/5/12 20:05
"""
import heapq

def meeting_rooms(tasks):
    s_tasks = sorted(tasks, key=lambda task: task[0])
    endings = [s_tasks[0][1]]
    heapq.heapify(endings)

    for start, end in s_tasks[1:]:
        if endings[0] <= start:
            heapq.heappop(endings)
            heapq.heappush(endings, end)
        else:
            heapq.heappush(endings, end)
    return len(endings)

if __name__ == "__main__":
    nums = [[0, 30], [5, 10], [15, 20]]
    print(meeting_rooms(nums))
    nums = [[7, 10], [2, 4]]
    print(meeting_rooms(nums))
    nums = [[7, 10], [2, 7]]
    print(meeting_rooms(nums))



