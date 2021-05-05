"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p282 file
Author: zhangxiaoan 00565442
Create: 2021/4/29 9:25
"""


def add_operators(num, target):
    n = len(num)
    ans = []

    def gen_expr(num, index, expr, prev_op, prev_value, value):
        nonlocal n, target, ans

        start = num[index]
        end = index
        while end < n:
            val = int(num[index:end + 1])
            expr.append(prev_op)
            expr.append(num[index:end + 1])


            if prev_op == '+':
                next_val = value + val
            if prev_op == '-':
                next_val = value - val
            if prev_op == '*':
                next_val = value + prev_value * val
                
            if end == n - 1:
                if next_val == target:
                    ans.append("".join(expr[1:]))
                
                expr.pop()
                expr.pop()
                return

            if prev_op == '+':
                gen_expr(num, end + 1, expr, "*", val, value)
            elif prev_op == '-':
                gen_expr(num, end + 1, expr, "*", -val, value)
            else:
                gen_expr(num, end + 1, expr, "*", prev_value * val, value)


            gen_expr(num, end + 1, expr, "+", 0, next_val)
            gen_expr(num, end + 1, expr, "-", 0, next_val)
            expr.pop()
            expr.pop()

            if start == '0':
                break

            end += 1

    gen_expr(num, 0, [], "+", 0, 0)
    return ans


if __name__ == "__main__":
    print(add_operators("123", 6))
    print(add_operators("232", 8))
    print(add_operators("105", 5))
    print(add_operators("00", 0))
    print(add_operators("3456237490", 9191))
    print(add_operators("134562379", 134562379))
    print(add_operators("123456789", 45))
