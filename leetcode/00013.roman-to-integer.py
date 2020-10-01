class Solution:
    def romanToInt(self, s: str) -> int:
        hash_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        r, i = 0, 0
        while i < len(s):
            value = hash_values[s[i]]
            next_value = hash_values[s[i+1]] if i+1 < len(s) else 0

            if next_value > value:
                r += next_value-value
                i += 2
            else:
                r += value
                i += 1
        return r


tests = [
    ('IV', 4),
    ('MCMXCIV', 1994),
]


for A,  r in tests:
    a = Solution().romanToInt(A)
    if a != r:
        print(f"\033[91m{A} -> {a} # {r}")
    else:
        print(f"\033[92m{A} -> OK")
