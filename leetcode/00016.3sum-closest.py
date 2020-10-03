from typing import List
import time


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                print(sum, '|', sum-target, '|',
                      f"{nums[i]} - {nums[lo]} - {nums[hi]}")
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff


tests = [
    ([[-1, 2, 1], 1], 2),
    ([[-1, 2, 1, -4], 1], 2),
    ([[1, 1, 1, 1], 0], 3),
    ([[1, 1, -1, -1, 3], 3], 3),
    ([[1, 1, 1, 0], -100], 2),
    ([[1, 1, 1, 1], -100], 3),
    ([[1, 2, 4, 8, 16, 32, 64, 128], 82], 82)

]

for A,  r in tests:
    start_time = time.time()
    a = Solution().threeSumClosest([*A[0]], A[1])
    exec_time = (time.time() - start_time)
    if a != r or exec_time > 1:
        print(f"\033[91m -> {a} # {r} | {exec_time}")
    else:
        print(f"\033[92m -> OK | {exec_time}")
