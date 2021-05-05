from collections import defaultdict


def least_bricks(wall):
    n = len(wall)
    prefix_nums = defaultdict(int)
    max_prefix_num = 0

    def line_prefix_sum(line):
        nonlocal prefix_nums, max_prefix_num
        
        cur_sum = 0
        for brick in line[:-1]:
            cur_sum += brick
            prefix_nums[cur_sum] += 1
            if prefix_nums[cur_sum] > max_prefix_num:
                max_prefix_num = prefix_nums[cur_sum]
    
    for line in wall:
        line_prefix_sum(line)
    
    return n - max_prefix_num

if __name__ == "__main__":
    wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
    print(least_bricks(wall))
    wall = [[1], [1], [1]]
    print(least_bricks(wall))

    
