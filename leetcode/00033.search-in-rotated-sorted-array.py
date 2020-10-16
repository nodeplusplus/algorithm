from typing import List


class Solution:
    # logn
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        # nlogn
        pivot = self.findPivot(nums, 0, len(nums)-1)
        if pivot == -1:
            return self.searchInBinary(nums, target, 0, len(nums)-1)

        if target == nums[pivot]:
            return pivot
        if nums[0] <= target:
            return self.searchInBinary(nums, target, 0, pivot-1)
        return self.searchInBinary(nums, target, pivot+1, len(nums)-1)

    def findPivot(self, nums, low, high):
        # base cases
        if high < low:
            return -1
        if high == low:
            return low

        # low + (high - low)/2;
        mid = int((low + high)/2)

        if mid < high and nums[mid] > nums[mid + 1]:
            return mid
        if mid > low and nums[mid] < nums[mid - 1]:
            return (mid-1)
        if nums[low] >= nums[mid]:
            return self.findPivot(nums, low, mid-1)
        return self.findPivot(nums, mid + 1, high)

    def searchInBinary(self, nums, target, low, high):
        if high < low:
            return -1

        mid = int((low + high)/2)

        if target > nums[mid]:
            return self.searchInBinary(nums, target, mid+1, high)
        if target < nums[mid]:
            return self.searchInBinary(nums, target, low, mid-1)

        return mid


# class Solution:
#     # nlogn
#     def search(self, nums: List[int], target: int, pivot=0) -> int:
#         if len(nums) == 1:
#             return 0 if nums[0] == target else -1

#         pivot = round(len(nums)/2)

#         left = self.search(nums[:pivot], target)
#         if left >= 0:
#             return left

#         right = self.search(nums[pivot:], target, pivot)
#         if right >= 0:
#             return right+pivot

#         return -1


tests = [
    # ([[0], 0], 0),
    # ([[0], 1], -1),
    # ([[4, 5, 6, 7, 0, 1, 2], 0], 4),
    ([[1, 3, 5], 1], 0),

]

for A,  r in tests:
    a = Solution().search(A[0], A[1])
    if a != r:
        print(f"\033[91m {A} -> {a} # {r}")
    else:
        print(f"\033[92m -> OK")
