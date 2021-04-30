"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p282 file
Author: zhangxiaoan 00565442
Create: 2021/4/29 9:25
"""


def add_operators(nums, target):
    n = len(nums)
    ans = set()

    def gen_expr(nums, index, expr, prev_op, prev_value, value):
        nonlocal n, target, ans
        if index == n:
            if (value == target and prev_op != '*' ) or (prev_op == "*" and prev_value + value == target):
                ans.add("".join(expr))
            return

        start = nums[index]

        end = index
        while end < n:
            val = int(nums[index:end + 1])
            expr.append(prev_op)
            expr.append(nums[index:end + 1])

            if prev_op == '+' or not prev_op:
                next_val = value + val
                gen_expr(nums, end + 1, expr, "*", val, value)
            elif prev_op == '-':
                next_val = value - val
                gen_expr(nums, end + 1, expr, "*", -val, value)
            else:
                next_val = value + prev_value * val
                gen_expr(nums, end + 1, expr, "*", prev_value * val, value)

            gen_expr(nums, end + 1, expr, "+", 0, next_val)
            gen_expr(nums, end + 1, expr, "-", 0, next_val)
            expr.pop()
            expr.pop()

            if start == '0':
                break
            end += 1

    gen_expr(nums, 0, [], "", 0, 0)
    return list(ans)


if __name__ == "__main__":
    print(add_operators("123", 6))
    print(add_operators("232", 8))
    print(add_operators("105", 5))
    print(add_operators("00", 0))
    print(add_operators("3456237490", 9191))
    print(add_operators("134562379", 134562379))
    print(add_operators("123456789", 45))
