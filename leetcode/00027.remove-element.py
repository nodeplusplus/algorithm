from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                continue
            i += 1

        return len(nums)


tests = [
    ([[0, 1, 2, 2, 3, 0, 4, 2], 2], 5)
]

for A,  r in tests:
    a = Solution().removeElement(A[0], A[1])
    if a != r:
        print(f"\033[91m -> {a} # {r}")
    else:
        print(f"\033[92m -> OK")
