"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p500.py file
Author: zhangxiaoan 00565442
Create: 2021/5/11 19:30
"""

def find_words(words):
    c_hash = {}
    for c in "qwertyuiop":
        c_hash[c] = 1

    for c in "asdfghjkl":
        c_hash[c] = 2

    for c in "zxcvbnm":
        c_hash[c] = 3

    ans = []
    for word in words:
        line = c_hash[word[0].lower()]
        b_ok = True
        for c in word[1:]:
            if c_hash[c.lower()] != line:
                b_ok = False
                break
        if b_ok:
            ans.append(word)
    return ans

if __name__ == "__main__":
    print(find_words(["Hello", "Alaska", "Dad", "Peace"]))


