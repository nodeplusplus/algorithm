from typing import List


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         if len(nums) <= 1:
#             return sum(nums)
#         ans = cur = nums[0]

#         for i in range(1, len(nums)):
#             if cur + nums[i] < nums[i]:
#                 cur = nums[i]
#             else:
#                 cur += nums[i]
#             ans = max(cur, ans)
#         return ans

# Another solution, fater than 5%
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxsofar = 0
#         a = []
#         maxending = 0
#         for i in range(len(nums)):
#             maxending = maxending + nums[i]
#             if maxending < 0:
#                 a.append(maxending)
#                 maxending = 0
#             elif maxsofar < maxending:
#                 maxsofar = maxending
#         if maxsofar == 0 and a != []:
#             return max(nums)
#         else:
#             return maxsofar

# Dynamic Programming
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return sum(nums)

        ans = [*nums]
        for i in range(1, len(ans)):
            ans[i] = max(ans[i-1]+nums[i], nums[i])

        return max(ans)


tests = [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([-2, 1], 1),
    ([-1, 0, -2], 0),
    ([-2, -1, -2], -1)
]


for A, r in tests:
    a = Solution().maxSubArray(A)

    if a != r:
        print(f"\033[91m -> {a} # {r}")
    else:
        print(f"\033[92m -> OK")
