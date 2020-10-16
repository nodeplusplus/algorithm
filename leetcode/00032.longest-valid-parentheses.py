class Solution:
    # DP
    def longestValidParentheses(self, s: str) -> int:
        dp, i = [0 for _ in range(len(s))], 1

        while i < len(s):
            p = s[i-1]
            c = s[i]
            # ..()
            if p == '(' and c == ')':
                dp[i] = dp[i-2] + 2

            # ..))
            if p == ')' and c == ')':
                # ..((..))..
                j = i-dp[i-1]-1
                # chainable
                # ..()((..))..
                k = j-1
                if j >= 0 and s[j] == '(':
                    dp[i] = dp[i-1]+dp[k]+2

            i += 1

        return max(dp) if len(dp) else 0

# class Solution:
#     # Stack
#     def longestValidParentheses(self, s: str) -> int:
#         if len(s) <= 1:
#             return 0

#         count, stack = 0, [-1]

#         for (i, char) in enumerate(s):
#             if char == '(':
#                 stack.append(i)

#             if char == ')':
#                 stack.pop()

#                 if len(stack):
#                     count = max(count, i-stack[-1])
#                 else:
#                     stack.append(i)

#         return count


tests = [
    ('', 0),
    ('(((', 0),
    ('(()', 2),
    ('()()()', 6),
    ('())(())', 4),
    (')()())', 4),
    ('()()())', 6),
    (')(()((', 2),
    ("()(()", 2),
    ("(())(()", 4),
    (")(())", 4),
    ("()((()))", 8),
    ("())((())", 4),
    ("(()))())(", 4)
]

for A,  r in tests:
    a = Solution().longestValidParentheses(A)
    if a != r:
        print(f"\033[91m {A} -> {a} # {r}")
    else:
        print(f"\033[92m -> OK")
