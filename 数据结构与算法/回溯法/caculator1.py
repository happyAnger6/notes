def caculator(s):
    def expr(s, i, n, prev_op, prev_val, value):
        left = i
        while i < n and '0' <= s[i] <= '9':
            i += 1
        val = int(s[left:i])
        if i == n:
            if prev_op == '*':
                return value + prev_val * val
            if prev_op == '/':
                return value + prev_val / val
            if prev_op == '-':
                return value - val
            if prev_op == '+':
                return value + val

        cur_op = s[i]
        if cur_op == '+' or cur_op == '-':
            if prev_op == '+':
                value += val
            if prev_op == '-':
                value -= val
            if prev_op == '*':
                value = value + prev_val * val
            if prev_op == '/':
                value = value + prev_val / val
            return expr(s, i + 1, n, cur_op, 0, value)

        if cur_op == '*' or cur_op == '/':
            if prev_op == '+':
                prev_val = val
            if prev_op == '-':
                prev_val = -val
            if prev_op == '*':
                prev_val = prev_val * val
            if prev_op == '/':
                prev_val = prev_val / val
            return expr(s, i + 1, n, cur_op, prev_val, value)
    n = len(s)
    if n == 0:
        return 0
    return expr(s, 0, n, '+', 0, 0)


if __name__ == "__main__":
    print(caculator("1+2*3"))
    print(caculator(""))
    print(caculator("0"))
    print(caculator("10"))
    print(caculator("10-2+3*3-4"))
    print(caculator("10+2-1+2*3*3-4+5"))
