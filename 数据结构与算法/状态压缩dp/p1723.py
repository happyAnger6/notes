def min_time_required(jobs, k):
    n = len(jobs)
    sub_jobs_times = [0 for _ in range(1<<n)]

    for i in range(1<<n):
        start, job = i, 0
        while start > 0:
            if start & 1 == 1:
                sub_jobs_times[i] += jobs[job]
            start >>= 1
            job += 1

    dp = [[0 for _ in range(1<<n)] for _ in range(k)]
    for i in range(1<<n):
        dp[0][i] = sub_jobs_times[i]

    for i in range(1, k):
        dp[i][0] = 0
        for j in range(1, 1<<n):
            min_cost = float("inf")
            x = j
            while x > 0:
                min_cost = min(min_cost, max(dp[i-1][j-x], sub_jobs_times[x]))
                x = (x-1)&j
            dp[i][j] = min_cost

    return dp[k-1][(1<<n)-1]

if __name__ == "__main__":
    print(min_time_required([3, 2, 3], 3))
    print(min_time_required([1, 2, 4, 7, 8], 2))
    jobs = [20010,20006,20014,20004,20008,20006,20005,20012,19999,20014,20003,20012]
    print(min_time_required(jobs, 8))
