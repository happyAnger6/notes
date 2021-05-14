def solve_NQueens(n):
    results = []
    def check(result, i):
        if i == 0:
            return True

        end_i, end_j = i, result[-1]
        for row, col in enumerate(result[:-1]):
            if abs(end_i-row) == abs(end_j-col):
                return False
        return True

    def change_results(results, n):
        new_results = []
        def new_result(result, n):
            new_result = []
            for v in result:
                s = ""
                for i in range(n):
                    if v == i:
                        s += 'Q'
                    else:
                        s += '.'
                new_result.append(s)
            return new_result

        for result in results:
            new_results.append(new_result(result, n))
        return new_results

    def do_line(i, s, result=None):
        nonlocal results

        if result is None:
            result = []

        if not s:
            results.append(result[:])
            return

        for pos in s:
            result.append(pos)
            if check(result, i):
                do_line(i+1, s-{pos}, result)
            result.pop()

    do_line(0, set(range(n)))
    return change_results(results, n)

if __name__ == "__main__":
    print(solve_NQueens(4))
    print(solve_NQueens(1))
    print(solve_NQueens(8))
