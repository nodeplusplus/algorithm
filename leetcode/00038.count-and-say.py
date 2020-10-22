class Solution:
    def countAndSay(self, n: int) -> str:
        chars = ''

        for _ in range(n):
            if not chars:
                chars = '1'
                continue

            newchars, char, count = '', '', 0
            for j in range(len(chars)):
                if char == chars[j]:
                    count += 1
                else:
                    if char:
                        newchars += str(count) + char
                    char = chars[j]
                    count = 1
            chars = newchars + str(count) + char

        return chars


tests = [
    (1, '1'),
    (2, '11'),
    (3, '21'),
    (4, '1211'),
    (5, '111221'),
    (6, '312211'),
    (7, '13112221'),
    (8, '1113213211'),
    (9, '31131211131221'),
    (10, '13211311123113112211'),
]

for A,  r in tests:
    a = Solution().countAndSay(A)
    if a != r:
        print(f"\033[91m {A} -> {a} # {r}")
    else:
        print(f"\033[92m -> OK")
