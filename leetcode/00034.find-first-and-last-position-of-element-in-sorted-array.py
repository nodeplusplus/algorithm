from typing import List


# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         if not len(nums):
#             return [-1, -1]
#         if len(nums) == 1:
#             return [0, 0] if nums[0] == target else [-1, -1]

#         left = self.searchLeft(nums, target, 0, len(nums)-1)
#         if left == -1:
#             return [-1, -1]
#         right = self.searchRight(nums, target, left, len(nums)-1)

#         return [left, right]

#     def searchLeft(self, nums: [int], target: int, l: int, r: int) -> int:
#         if l > r:
#             return -1
#         m = l + (r - l) // 2

#         if target < nums[m]:
#             return self.searchLeft(nums, target, l, m-1)
#         if target > nums[m]:
#             return self.searchLeft(nums, target,  m+1, r)

#         if m == 0:
#             return m

#         if nums[m-1] == target:
#             return self.searchLeft(nums, target, l, m-1)

#         return m

#     def searchRight(self, nums: [int], target: int, l: int, r: int) -> int:
#         if l > r:
#             return -1

#         m = l + (r - l) // 2

#         if target < nums[m]:
#             return self.searchRight(nums, target, l, m-1)
#         if target > nums[m]:
#             return self.searchRight(nums, target,  m+1, r)

#         if m == len(nums)-1:
#             return m

#         if nums[m+1] == target:
#             return self.searchRight(nums, target,  m+1, r)

#         return m

class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo

    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]


tests = [
    ([[5, 7, 7, 8, 8, 10], 8], [3, 4]),
    ([[5, 7, 7, 8, 8, 10, 12], 8], [3, 4]),
    ([[5, 7, 7, 8, 8, 10, 12, 15], 8], [3, 4]),
    ([[5, 7, 7, 8, 8, 10], 6], [-1, -1]),
    ([[5, 8, 8, 8, 8, 8, 8, 8, 8, 13], 8], [1, 8]),
    ([[8, 8, 8, 8, 8, 8, 8, 8, 8, 8], 8], [0, 9]),
    ([[1, 4], 1], [0, 0]),
    ([[1, 4], 4], [1, 1]),
    ([[4, 4], 4], [0, 1]),
    ([[1, 2, 3], 1], [0, 0]),
    ([[], 0], [-1, -1])
]

for A,  r in tests:
    a = Solution().searchRange(A[0], A[1])
    if a != r:
        print(f"\033[91m {A} -> {a} # {r}")
    else:
        print(f"\033[92m -> OK")
