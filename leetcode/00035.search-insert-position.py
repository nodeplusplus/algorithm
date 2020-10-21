from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.searchInBinary(nums, target, 0, len(nums)-1)

    def searchInBinary(self, nums: List[int], target: int, l: int, r: int) -> int:
        if l == r:
            return l+1 if nums[l] < target else l
        if target <= nums[l]:
            return l
        if target >= nums[r]:
            return r if target == nums[r] else r+1

        m = l + (r - l) // 2

        if target > nums[m]:
            return self.searchInBinary(nums, target, m+1, r)

        if target < nums[m]:
            return self.searchInBinary(nums, target, l, m-1)

        return m


tests = [
    ([[1, 3, 5, 6], 5], 2),
    ([[1, 3, 5, 6], 2], 1),
    ([[1, 3, 5, 6], 7], 4),
    ([[1, 3, 5, 6], 0], 0),
    ([[1], 1], 0),
    ([[1, 3], 2], 1),
    ([[1, 3], 3], 1),
    ([[1, 3, 5, 6], 7], 4),
    ([[3, 5, 7, 9, 10], 8], 3),
]

for A,  r in tests:
    a = Solution().searchInsert(A[0], A[1])
    if a != r:
        print(f"\033[91m {A} -> {a} # {r}")
    else:
        print(f"\033[92m -> OK")
