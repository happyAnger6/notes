def num_tress(n):
    dp = [0 for _ in range(n+1)]

    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-1-j]
    
    return dp[n]

def num_tress1(n):
    if n < 1:
        return 0

    c = 1
    for i in range(n):
        c = c * 2 * (2 * i + 1) // (i + 2)

    return c

if __name__ == "__main__":
    print(num_tress(3))
    print(num_tress1(3))