from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Index is in asc order
        hash_sums = {}

        # n^2
        for i in range(len(nums)):
            x, j = nums[i], i+1
            while j < len(nums):
                y = nums[j]
                s = x+y
                h = {i: x, j: y}
                if s in hash_sums.keys():
                    if h not in hash_sums[s]:
                        hash_sums[s].append(h)
                else:
                    hash_sums[s] = [h]
                j += 1

        # n -> 2sum
        sets = []
        keys, i, j = sorted(list(hash_sums.keys())), 0, len(hash_sums)-1

        while i <= j:
            left = keys[i]
            right = keys[j]

            s = left+right
            if s == target:
                for l in hash_sums[left]:
                    for r in hash_sums[right]:
                        # Make sure we don't use an index multi times
                        _set = sorted(list({**l, **r}.values()))
                        if len(_set) == 4 and _set not in sets:
                            sets.append(_set)
            if s > target:
                j -= 1
            else:
                i += 1

        return sorted(sets)


tests = [
    (
        [[1, 0, -1, 0, -2, 2], 0],
        sorted([
            [-1,  0, 0, 1],
            [-2, -1, 1, 2],
            [-2,  0, 0, 2]
        ])
    ),
    ([[0, 0, 0, 0], 0], [[0, 0, 0, 0]]),
    ([[-2, -1, -1, 1, 1, 2, 2], 0], sorted([[-2, -1, 1, 2], [-1, -1, 1, 1]]))
]

for A,  r in tests:
    a = Solution().fourSum(A[0], A[1])
    if a != r:
        print(f"\033[91m -> {a} # {r}")
    else:
        print(f"\033[92m -> OK")
