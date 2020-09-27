class Solution:
    def myAtoi(self, str: str) -> int:
        a = '0123456789'
        if len(str) == 1 and str not in a:
            return 0

        INT_MIN, INT_MAX = -(2 ** 31), (2 ** 31)-1
        r = ''

        for c in str:
            if c == ' ' and not r:
                continue

            if not r and (c == '-' or c == '+'):
                r += c
            elif c not in a:
                break

            if c in a:
                r += c

        if len(r) < 1:
            return 0
        if r == '-' or r == '+':
            return 0

        if int(r) < INT_MIN:
            return INT_MIN
        if int(r) > INT_MAX:
            return INT_MAX
        return int(r)


tests = [
    ("42", 42),
    ("+-42", 0),
    ("   -42", -42),
    ("   +42", 42),
    ("   +0 123", 0),
    ("4193 with 1 words", 4193),
    ("words and 987", 0),
    ("-91283472332", -2147483648),
    ("-91283-472332", -91283),
]


for t,  r in tests:
    a = Solution().myAtoi(t)
    if a != r:
        print(f"{a} # {r}")
