from collections import Counter


def delete_and_earn(nums):
    counter = Counter(nums)
    s_counter = sorted(counter.items(), key=lambda m: m[0])
    n = len(s_counter)

    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = s_counter[0][0] * s_counter[0][1]

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        if s_counter[i][0] == s_counter[i-1][0] + 1:
            dp[i][1] = dp[i-1][0] + s_counter[i][0] * s_counter[i][1]
        else:
            dp[i][1] = dp[i][0] + s_counter[i][0] * s_counter[i][1]

    return max(dp[n-1][0], dp[n-1][1])

if __name__ == "__main__":
    print(delete_and_earn([3, 4, 2]))
    print(delete_and_earn([2, 2, 3, 3, 3, 4]))




