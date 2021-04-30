"""
Copyright (c) Huawei Technologies Co., Ltd. 2021-2021. All rights reserved.
Description: easy_ut p30 file
Author: zhangxiaoan 00565442
Create: 2021/4/27 17:33
Q: 30.串联所有单词的子串(https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/)
"""
from collections import Counter
def findSubstring(s, words):
    if not words:
        return []

    n, m = len(s), len(words[0])
    results =[]
    i = 0
    while i < m:
        left = i
        word_cnts = Counter(words)
        cur_word_cnts = Counter()
        start = left
        for right in range(start, n-m+1, m):
            word = s[right:right+m]

            if word in word_cnts:
                cur_word_cnts[word] += 1

            if cur_word_cnts[word] > word_cnts[word] or right - left >= m*len(words) or word not in word_cnts:
                word = s[left:left + m]
                if word in word_cnts:
                    cur_word_cnts[word] -= 1
                left += m

            if word_cnts == cur_word_cnts:
                results.append(left)
        i += 1
    return results

if __name__ == "__main__":
    print(findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print(findSubstring("barfoofoobarthefoobarman", ["foo", "bar", "the"]))
    print(findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))






