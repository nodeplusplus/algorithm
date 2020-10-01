from typing import List


# class Solution:
#     # Vertical scanning
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not len(strs):
#             return ''

#         r, i, length = '', 0, len(strs)

#         while True:
#             t = ''
#             for string in strs:
#                 if i >= len(string):
#                     return r
#                 if t and string[i] not in t:
#                     return r

#                 t += string[i]

#             if len(t) != length:
#                 return r
#             r += t[0]
#             i += 1

#         return r


# class Solution:
#     # Horizontal scanning
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not len(strs):
#             return ''

#         r = strs.pop(0)
#         for i in range(len(strs)):
#             current_str = strs[i]

#             if not r or not current_str:
#                 return ''

#             for j in range(len(r)):
#                 if j >= len(current_str) or r[j] != current_str[j]:
#                     r = r[:j]
#                     break

#         return r


class Solution:
    # Divide and conquer
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ''
        if len(strs) == 1:
            return strs[0]

        pivot = round(len(strs)/2)
        left = self.longestCommonPrefix(strs[:pivot])
        right = self.longestCommonPrefix(strs[pivot:])

        r = ''
        for i in range(len(left)):
            if i >= len(right) or left[i] != right[i]:
                break
            r += left[i]

        return r


tests = [
    (["flower", "flow", "flight"], 'fl'),
    (["dog", "racecar", "car"], ''),
    (["flower", "flow", ""], ''),
]


for A,  r in tests:
    a = Solution().longestCommonPrefix([*A])
    if a != r:
        print(f"\033[91m{A} -> {a} # {r}")
    else:
        print(f"\033[92m{A} -> OK")
