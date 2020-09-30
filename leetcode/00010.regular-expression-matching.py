# A big note: you shouldn't read any line of this problem, a f*cking prolem =))

# Recursive
class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            skip_asterisk_matched = self.isMatch(text, pattern[2:])
            keep_asterisk_matched = first_match and self.isMatch(
                text[1:], pattern)
            return skip_asterisk_matched or keep_asterisk_matched
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

# Dynamic Programming
# class Solution(object):
#     def isMatch(self, text, pattern):
#         memo = {}

#         def dp(i, j):
#             if (i, j) not in memo:
#                 if j == len(pattern):
#                     ans = i == len(text)
#                 else:
#                     first_match = i < len(text) and pattern[j] in {
#                         text[i], '.'}
#                     if j+1 < len(pattern) and pattern[j+1] == '*':
#                         ans = dp(i, j+2) or first_match and dp(i+1, j)
#                     else:
#                         ans = first_match and dp(i+1, j+1)

#                 memo[i, j] = ans
#             return memo[i, j]

#         return dp(0, 0)


tests = [
    ('abcdefghd', 'ab.*c', False),
]


for s, p,  r in tests:
    a = Solution().isMatch(s, p)
    if a != r:
        print(f"{s} | {p} -> {a} # {r}")
