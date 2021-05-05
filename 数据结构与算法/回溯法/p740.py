from collections import Counter

def delete_and_earn(nums):
    max_score = 0
    num_counter = Counter(nums)
    sorted_num_counter = sorted(num_counter.items(), key=lambda m: m[0])

    def deal_one(nums, prev_status, i, n, score=0):
        nonlocal max_score
        if i == n:
            if score > max_score:
                max_score = max(max_score, score)
            return

        val, num = nums[i] 
        if prev_status == 0 or nums[i-1][0] < val - 1: # no delete or no sense
            deal_one(nums, 1, i+1, n, score + val * num)
            deal_one(nums, 0, i+1, n, score)
        else:
            deal_one(nums, 0, i+1, n, score)

    deal_one(sorted_num_counter, 0, 0, len(sorted_num_counter))
    return max_score

if __name__ == "__main__":
    print(delete_and_earn([3, 4, 2]))
    print(delete_and_earn([2, 2, 3, 3, 3, 4]))
    nums = [12,32,93,17,100,72,40,71,37,92,58,34,29,78,11,84,77,90,92,35,12,5,27,92,91,23,65,91,85,14,42,28,80,85,38,71,62,82,66,3,33,33,55,60,48,78,63,11,20,51,78,42,37,21,100,13,60,57,91,53,49,15,45,19,51,2,96,22,32,2,46,62,58,11,29,6,74,38,70,97,4,22,76,19,1,90,63,55,64,44,90,51,36,16,65,95,64,59,53,93]
    print(delete_and_earn(nums))

        
