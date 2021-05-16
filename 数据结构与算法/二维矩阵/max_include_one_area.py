def max_include_one_area(matrix, x, y):
    rows, cols = len(matrix), len(matrix[0])
    max_area = 0

    cols_prefix_one_nums = [[0 for _ in range(cols)] for _ in range(rows+1)]
    for col in range(cols):
        for row in range(rows):
            cols_prefix_one_nums[row+1][col] = cols_prefix_one_nums[row][col] + matrix[row][col]

    def one_col_nums(i_row, j_row, i_col):
        nonlocal cols_prefix_one_nums
        return cols_prefix_one_nums[j_row][i_col] - cols_prefix_one_nums[i_row][i_col]

    for start_row in range(x+1):
        for end_row in range(x, rows):
            height = end_row - start_row + 1
            left, right = 0, y
            one_nums = 0
            for i in range(left, right+1):
                one_nums += one_col_nums(start_row, end_row+1, i)

            while left <= right and right < cols:
                if one_nums == 1:
                    area = (right - left + 1) * height
                    max_area = max(max_area, area)
                    right += 1
                    if right < cols:
                        one_nums += one_col_nums(start_row, end_row+1, right)
                else:
                    one_nums -= one_col_nums(start_row, end_row+1, left)
                    left += 1

    return max_area

if __name__ == "__main__":
    matrix = [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0]
    ]
    print(max_include_one_area(matrix, 1, 2))
    
    matrix = [
        [0, 1, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0]
    ]
    print(max_include_one_area(matrix, 1, 2))