class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        n1, n2 = 0, 0

        # The ord() function returns an integer representing the Unicode character.
        for i in num1:
            n1 = n1*10 + ord(i)-48
        for j in num2:
            n2 = n2*10 + ord(j)-48

        return str(n1 * n2)


tests = [
    ('100', '123'),
    ('123', '456'),
    ('99', '1'),
]

for num1, num2 in tests:
    a = Solution().multiply(num1, num2)
    r = str(int(num1) * int(num2))
    if a != r:
        print(f"\033[91m {num1} + {num2} -> {a} # {r}")
    else:
        print(f"\033[92m -> OK")
