"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p1849 file
Author: zhangxiaoan 00565442
Create: 2021/5/7 9:09
"""

def splitString(s):
    def split(s, pre_num=None):
        n = len(s)
        if n == 0:
            return False

        if pre_num is not None and int(s) + 1 == pre_num:
            return True

        for i in range(n):
            cur_num = int(s[:i + 1])
            if pre_num is None:
                if split(s[i + 1:], cur_num):
                    return True
            elif cur_num + 1 != pre_num:
                continue
            else:
                if i == n - 1 or split(s[i+1:], cur_num):
                    return True

        return False
    return split(s)

if __name__ == "__main__":
    print(splitString("1234"))
    print(splitString("0090089"))
    print(splitString("050043"))
    print(splitString("9080701"))
    print(splitString("10009998"))
