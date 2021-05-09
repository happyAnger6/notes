from collections import deque


def num_islands(grid):
    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    visited = set()
    rows, cols = len(grid), len(grid[0])

    def bfs_point(point, grid):
        nonlocal dirs, visited, rows, cols
        x, y = point
        if grid[x][y] == "0":
            return 0

        if (x, y) in visited:
            return 0

        q = deque()
        q.append(point)
        visited.add((x, y))
        while q:
            n = len(q)
            while n > 0:
                n -= 1
                point = q.popleft()

                x, y = point
                for dir_ in dirs:
                    dir_x, dir_y = dir_
                    next_x, next_y = x + dir_x, y + dir_y
                    if next_x < 0 or next_x >= rows:
                        continue
                    
                    if next_y < 0 or next_y >= cols:
                        continue
                    
                    if grid[next_x][next_y] == "0":
                        continue

                    if (next_x, next_y) in visited:
                        continue

                    visited.add((next_x, next_y))
                    q.append((next_x, next_y))
        return 1

    total = 0
    for row in range(rows):
        for col in range(cols):
            total += bfs_point((row, col), grid)
    return total

if __name__ == "__main__":
    grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    print(num_islands(grid))

    grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

    print(num_islands(grid))






        

