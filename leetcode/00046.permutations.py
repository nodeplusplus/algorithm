from typing import List
from itertools import permutations
from collections import Counter


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) == 1:
#             return [nums]

#         ans = []

#         def backtrack(a, l, r):
#             if l == r:
#                 if a not in ans:
#                     ans.append(a)
#             else:
#                 for i in range(l, r+1):
#                     a[l], a[i] = a[i], a[l]
#                     backtrack([*a], l+1, r)
#                     a[l], a[i] = a[i], a[l]  # backtrack
#         backtrack(nums, 0, len(nums)-1)
#         return sorted(ans)

# # Magic here
# class Solution:  # DFS
#     def permute(self, nums):
#         res = []
#         self.dfs(nums, [], res)
#         return res

#     def dfs(self, nums, path, res):
#         if not nums:
#             res.append(path)
#             # return # backtracking
#         for i in range(len(nums)):
#             self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results


tests = [
    [1, 2, 3],
    [1, 2, 3, 4],
]

# 1 2 3
# 2 1 3
# 3 1 2
# 3 2 1

for A in tests:
    a = Solution().permute(A)
    r = [list(_r) for _r in list(permutations(A))]
    if a != r:
        print(f"\033[91m -> {a} # {r}")
    else:
        print(f"\033[92m -> OK")
