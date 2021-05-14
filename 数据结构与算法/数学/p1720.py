"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p1720 file
Author: zhangxiaoan 00565442
Create: 2021/5/6 20:50
"""

def decode(encoded, first):
    encode = [first]
    for e in encoded:
        encode.append(e ^ encode[-1])
    return encode

if __name__ == "__main__":
    print(decode([1, 2, 3], 1))
    print(decode([6, 2, 7, 3], 4))
