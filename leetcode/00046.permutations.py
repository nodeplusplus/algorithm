from typing import List
import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        ans = []

        def backtrack(a, l, r):
            if l == r:
                if a not in ans:
                    ans.append(a)
            else:
                for i in range(l, r+1):
                    a[l], a[i] = a[i], a[l]
                    backtrack([*a], l+1, r)
                    a[l], a[i] = a[i], a[l]  # backtrack
        backtrack(nums, 0, len(nums)-1)
        return sorted(ans)


tests = [
    [1, 2, 3],
    # [1, 2, 3, 4],
]

# 1 2 3
# 2 1 3
# 3 1 2
# 3 2 1

for A in tests:
    a = Solution().permute(A)
    r = [list(_r) for _r in list(itertools.permutations(A))]
    if a != r:
        print(f"\033[91m -> {a} # {r}")
    else:
        print(f"\033[92m -> OK")
