from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key in h.keys():
                h[key].append(str)
            else:
                h[key] = [str]
        return list(h.values())


tests = [
    (
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    )
]


for A, r in tests:
    a = Solution().groupAnagrams(A)
    if a != r:
        print(f"\033[91m -> {a} # {r}")
    else:
        print(f"\033[92m -> OK")
