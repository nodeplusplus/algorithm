from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates) < target:
            return []

        candidates.sort(reverse=True)

        ans = []

        def backtrack(items: List[int], candidates: List[int], remain: int):
            if sum(items) >= target or remain <= 0 or not len(candidates):
                i = sorted(items)
                if sum(i) == target and i not in ans:
                    ans.append(i)
                return

            if remain >= candidates[0]:
                backtrack([*items,  candidates[0]],
                          candidates[1:], remain-candidates[0])

            return backtrack(items, candidates[1:], remain)

        backtrack([], candidates,  target)
        return sorted(ans)


tests = [
    # ([[10, 1, 2, 7, 6, 1, 5], 8], [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
    ([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 27], [])
]

for A,  r in tests:
    a = Solution().combinationSum(A[0], A[1])
    if a != r:
        print(f"\033[91m {A} -> {a} # {r}")
    else:
        print(f"\033[92m -> OK")
