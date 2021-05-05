def min_cost2(costs):
    n, k = len(costs), len(costs[0])
    min_costs = [[0 for _ in range(k)] for _ in range(n)]

    for i in range(k):
        min_costs[0][i] = costs[0][i]

    for i in range(1, n):
        for j in range(k):
            min_costs[i][j] = min(min_costs[i-1][:j] + min_costs[i-1][j+1:]) + costs[i][j] 
    return min(min_costs[n-1])

if __name__ == "__main__":
    print(min_cost2([[1, 5, 3], [2, 9, 4]]))


