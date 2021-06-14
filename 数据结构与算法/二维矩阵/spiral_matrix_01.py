import asyncio
def spiral_order(matrix):
    res = []
    while matrix:
        # 削头（第一层）
        res += matrix.pop(0)
        # 将剩下的逆时针转九十度，等待下次被削
        matrix = list(zip(*matrix))[::-1]
    return res

if __name__ == "__main__":
    print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

