"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p1734 file
Author: zhangxiaoan 00565442
Create: 2021/5/11 19:10
"""

def decode(encoded):
    n = len(encoded)
    decode = []
    i = 0
    while i < n-1:
        decode.append(encoded[i]^encoded[i+1])
        i += 1
    decode.append(decode[-1]^encoded[n-1])
    return [decode[0]^encoded[0]] + decode

if __name__ == "__main__":
    print(decode([3, 1]))
    print(decode([6, 5, 4, 6]))


