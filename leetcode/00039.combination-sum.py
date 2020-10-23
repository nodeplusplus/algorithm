from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)

        ans = []

        def backtrack(items: List[int], candidates: List[int], remain: int):
            if sum(items) >= target or remain <= 0 or not len(candidates):
                if sum(items) == target:
                    ans.append(sorted(items))
                return

            if remain >= candidates[0]:
                backtrack([*items,  candidates[0]],
                          candidates, remain-candidates[0])

            return backtrack(items, candidates[1:], remain)

        backtrack([], candidates,  target)
        return sorted(ans)


tests = [
    ([[2, 3, 5], 8], [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    ([[2, 3, 6, 7], 7], [[2, 2, 3], [7]]),
    ([[2], 1], []),
    ([[1], 1], [[1]]),
    ([[1], 2], [[1, 1]])
]

for A,  r in tests:
    a = Solution().combinationSum(A[0], A[1])
    if a != r:
        print(f"\033[91m {A} -> {a} # {r}")
    else:
        print(f"\033[92m -> OK")
