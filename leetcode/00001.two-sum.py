from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num = nums[i]
            t = target - num
            try:
                j = nums.index(t, i+1)
                if j > i:
                    return [i, j]
            except:
                continue
        return []

# Best solution
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hash = {}
#         for i in range(len(nums)):
#             num = nums[i]
#             if num in hash:
#                 return [hash[num], i]

#             hash[target - num] = i

#         return []
