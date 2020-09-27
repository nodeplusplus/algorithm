# Don't convert number to string -> challenge
import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True

        if x % 10 == 0:
            return False

        digits = int(math.log10(x))
        cur = digits/2
        frac, whole = math.modf(cur)
        i, j = 0, 0
        if frac == 0.5:
            j = whole
            i = whole+1
        else:
            i = whole+1
            j = whole-1

        while cur >= 0.5:
            l = math.floor(x / 10**i) % 10
            r = math.floor(x / 10**j) % 10
            if l != r:
                return False

            i += 1
            j -= 1
            cur -= 1

        return True


tests = [
    (-1, False),
    (0, True),
    (9, True),
    (121, True),
    (21212, True),
    (3212123, True),
    (3212124, False),
    (1221, True),
    (12121, True),
    (121121, True),
    (1211212, False),
    (120, False),
    (122, False),
    (1000021, False),
    (1000110001, True),
]


for t,  r in tests:
    a = Solution().isPalindrome(t)
    if a != r:
        print(f"{a} # {r}")
