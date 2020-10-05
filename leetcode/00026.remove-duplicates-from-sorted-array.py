from typing import List

# VKL, Leetcode use array reference
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         h = {}
#         for num in nums:
#             h[num] = num
#         return len(h)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        h, i = {}, 0
        while i < len(nums):
            if nums[i] in h:
                del nums[i]
                continue
            h[nums[i]] = i
            i += 1

        return len(h)


tests = [
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5)
]

for A,  r in tests:
    a = Solution().removeDuplicates(A)
    if a != r:
        print(f"\033[91m -> {a} # {r}")
    else:
        print(f"\033[92m -> OK")
