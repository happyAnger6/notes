class NumMatrix:
    def __init__(self, matrix) -> None:
        rows, cols = len(matrix), len(matrix[0])
        self.prefix_sums = [[0 for _ in range(cols + 1)] \
                    for _ in range(rows+1)]

        for row in range(1, rows+1):
            for col in range(1, cols+1):
                self.prefix_sums[row][col] = self.prefix_sums[row-1][col] + \
                self.prefix_sums[row][col-1] - self.prefix_sums[row-1][col-1] + \
                    + matrix[row-1][col-1]


    def sumRegion(self, row1, col1, row2, col2):
        return self.prefix_sums[row2+1][col2+1] - self.prefix_sums[row1][col2+1] \
            - self.prefix_sums[row2+1][col1] + self.prefix_sums[row1][col1]

if __name__ == "__main__":
    matrix =  [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

    nm = NumMatrix(matrix)
    print(nm.sumRegion(2, 1, 4, 3))
    print(nm.sumRegion(1, 1, 2, 2))
    print(nm.sumRegion(1, 2, 2, 4))
