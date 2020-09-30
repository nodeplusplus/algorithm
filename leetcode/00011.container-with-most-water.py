from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area, h = 0, 0

        i, j = 0, len(height)-1
        while i < j:
            w = j-i
            h = min(height[i], height[j])

            area = max(area, w*h)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return area


tests = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([3, 9, 3, 4, 7, 2, 12, 6], 45),
    ([1, 2, 1], 2),
]


for A,  r in tests:
    a = Solution().maxArea(A)
    if a != r:
        print(f"\033[91m{A} -> {a} # {r}")
    else:
        print(f"\033[92m{A} -> OK")
