def ship_with_days(weights, D):
    def check_ok(cap, weights, D):
        left_cap = cap
        i, n = 0, len(weights)
        while i < n and D > 0:
            if left_cap >= weights[i]:
                left_cap -= weights[i]
                i += 1
            else:
                if left_cap == cap:
                    break
                D -= 1
                left_cap = cap
        return i == n and D > 0
    
    left, right = 1, sum(weights)
    while left < right:
        mid = left + (right - left) // 2
        if check_ok(mid, weights, D):
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == "__main__":
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    D = 5
    print(ship_with_days(weights, D))
    weights = [3, 2, 2, 4, 1, 4]
    D = 3
    print(ship_with_days(weights, D))

            
            