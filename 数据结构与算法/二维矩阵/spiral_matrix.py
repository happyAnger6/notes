def spiral_order(matrix):
    results = []
    rows, cols = len(matrix), len(matrix[0])
    def print_one_spiral(matrix, up_row, down_row, left_col, right_col):
        nonlocal results
        col = left_col
        while col < right_col + 1:
            results.append(matrix[up_row][col])
            col += 1

        row = up_row + 1
        if row > down_row:
            return

        while row < down_row + 1:
            results.append(matrix[row][right_col])
            row += 1

        col = right_col - 1
        while col >= left_col:
            results.append(matrix[down_row][col])
            col -= 1

        row = down_row - 1
        while row > up_row:
            results.append(matrix[row][left_col])
            row -= 1

    row, col = 0, 0
    while rows > 0 and cols > 0:
        print_one_spiral(matrix, row, row+rows-1, col, col+cols-1)
        rows -= 2
        cols -= 2
        row += 1
        col += 1
    return results

if __name__ == "__main__":
    print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

