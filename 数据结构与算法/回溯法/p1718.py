def construct_distance_sequence(n):
    seq_len = (n-1)*2 + 1
    seq = [0 for _ in range(seq_len)]
    nums = [0 for _ in range(n)]

    def construct(seq, seq_len, pos, nums, left):
        nonlocal n
        if pos == seq_len:
            return True

        if seq[pos] != 0:
            if construct(seq, seq_len, pos+1, nums, left):
                return True
            return False

        right = n
        while right > 0:
            if nums[right-1] == 0:
                if right == 1:
                    seq[pos] = 1
                    nums[0] = 1
                    if construct(seq, seq_len, pos+1, nums, left-1):
                        return True
                    seq[pos] = 0
                    nums[0] = 0
                elif pos + right < seq_len and seq[pos+right] == 0:
                    seq[pos], seq[pos+right] = right, right
                    nums[right-1] = right 
                    if construct(seq, seq_len, pos+1, nums, left-1):
                        return True
                    nums[right-1] = 0
                    seq[pos], seq[pos+right] = 0, 0
            right -= 1
        return False

    construct(seq, seq_len, 0, nums, n)
    return seq

if __name__ == "__main__":
    print(construct_distance_sequence(3))
    print(construct_distance_sequence(5))

