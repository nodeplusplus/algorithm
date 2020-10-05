from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        base = '()'
        if n == 1:
            return [base]

        sets, childs = [], self.generateParenthesis(n-1)

        for child in childs:
            # Move from left to right
            for i in range(len(child)+1):
                if i == 0:
                    s = base+child
                    if s not in sets:
                        sets.append(s)

                else:
                    s = child[:i] + base + child[i:]
                    if s not in sets:
                        sets.append(s)

        return sets

# # Backtrack
# class Solution(object):
#     def generateParenthesis(self, N):
#         ans = []

#         def backtrack(S='', left=0, right=0):
#             if len(S) == 2 * N:
#                 ans.append(S)
#                 return
#             if left < N:
#                 backtrack(S+'(', left+1, right)
#             if right < left:
#                 backtrack(S+')', left, right+1)

#         backtrack()
#         return ans

# # Closure Number
# class Solution(object):
#     def generateParenthesis(self, N):
#         if N == 0:
#             return ['']
#         ans = []
#         for c in range(N):
#             for left in self.generateParenthesis(c):
#                 for right in self.generateParenthesis(N-1-c):
#                     ans.append('({}){}'.format(left, right))
#         return ans


tests = [
    # (1, ['()']),
    # (2, ['(())', '()()']),
    # (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    (
        4,
        [
            "(((())))", "((()()))", "((())())", "((()))()",
            "(()(()))", "(()()())", "(()())()", "(())(())",
            "(())()()", "()((()))", "()(()())", "()(())()",
            "()()(())", "()()()()"
        ]
    )
]

for A,  r in tests:
    a = Solution().generateParenthesis(A)
    if sorted(a) != sorted(r):
        print(f"\033[91m -> {' | '.join(sorted(a))} # {' | '.join(sorted(r))}")
    else:
        print(f"\033[92m -> OK")
