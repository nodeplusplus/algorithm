from typing import List


class Solution:
    # Vertical scanning
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ''

        r, i, length = '', 0, len(strs)

        while True:
            t = ''
            for string in strs:
                if i >= len(string):
                    return r
                if t and string[i] not in t:
                    return r

                t += string[i]

            if len(t) != length:
                return r
            r += t[0]
            i += 1

        return r


tests = [
    (["flower", "flow", "flight"], 'fl'),
    (["dog", "racecar", "car"], '')
]


for A,  r in tests:
    a = Solution().longestCommonPrefix(A)
    if a != r:
        print(f"\033[91m{A} -> {a} # {r}")
    else:
        print(f"\033[92m{A} -> OK")
