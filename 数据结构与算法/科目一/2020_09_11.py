"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut 2020_09_11 file
Author: zhangxiaoan 00565442
Create: 2021/5/11 19:41
"""

def decode_s(decode):
    stack = []
    num = 0
    for c in decode:
        if 'a' <= c <= 'z':
            stack.append(c)
        elif c == '(':
            stack.append('(')
        elif c == ')':
            sub_str = ""
            while stack and 'a' <= stack[-1] <= 'z':
                sub_str += stack.pop()
            stack.pop()
            stack.append(sub_str)
        elif c == '<':
            num = 0
        elif '0' <= c <= '9':
            num = num * 10 + int(c)
        elif c == '>':
            s = stack.pop()
            stack.append(s*num)

    s = ""
    while stack:
        s += stack.pop()
    return s[::-1]

if __name__ == "__main__":
    print(decode_s("abc(d)<2>e"))
    print(decode_s("a(b(c)<3>d)<2>e"))
