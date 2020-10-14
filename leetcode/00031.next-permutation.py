from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        i = len(nums)-2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = len(nums)-1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            self.swap(nums, i, j)

        k, h = i+1, len(nums)-1
        while k < h:
            self.swap(nums, k, h)
            k += 1
            h -= 1

        return

    def swap(self, nums, i, j):
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t


tests = [
    # ([1], [1]),
    # ([1, 2], [2, 1]),
    # ([1, 2, 3], [1, 3, 2]),
    ([5, 1, 1], [1, 1, 5]),
    # ([1, 3, 2, 5, 4, 6, 0], [1, 3, 2, 5, 6, 0, 4]),


]

for A,  r in tests:
    a = [*A]
    Solution().nextPermutation(a)
    if a != r:
        print(f"\033[91m -> {a} # {r}")
    else:
        print(f"\033[92m -> OK")
