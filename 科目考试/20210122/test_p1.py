from p1 import Solution

def test_pre_select():
    nums = [1, 2, 1]
    scores = [67, 58, 89, 42, 27]
    preference = [[0, 1], [1], [0, 2], [2], [0]]

    assert Solution().employee(nums, scores, preference) == [1, 2]