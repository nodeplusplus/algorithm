class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []
        open_brackets = ['(', '{', '[']
        close_brackets = [')', '}', ']']

        for char in s:
            if char in open_brackets:
                stack.append(char)

            if char in close_brackets:
                if not len(stack):
                    return False
                index = open_brackets.index(stack.pop())
                if char != close_brackets[index]:
                    return False
        return len(stack) == 0


tests = [
    ('()', True),
    ('(){}[]', True),
    ('(', False),
    ('(]', False),
    ('({[]})', True),
    ('([)]', False),
    ('((', False),
    (')(', False)
]

for A,  r in tests:
    a = Solution().isValid(A)
    if a != r:
        print(f"\033[91m -> {a} # {r}")
    else:
        print(f"\033[92m -> OK")
