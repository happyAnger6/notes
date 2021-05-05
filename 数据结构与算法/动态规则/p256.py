def min_cost(costs):
    n = len(costs)
    min_costs = [[0 for _ in range(3)] for _ in range(n)]
    min_costs[0][0] = costs[0][0]
    min_costs[0][1] = costs[0][1]
    min_costs[0][2] = costs[0][2]

    for i in range(1, n):
        min_costs[i][0] = min(min_costs[i-1][1], min_costs[i-1][2]) + costs[i][0] 
        min_costs[i][1] = min(min_costs[i-1][0], min_costs[i-1][2]) + costs[i][1]
        min_costs[i][2] = min(min_costs[i-1][0], min_costs[i-1][1]) + costs[i][2]
    return min(min_costs[n-1])

if __name__ == "__main__":
    print(min_cost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))


