from decimal import Decimal


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        r = self.pow(x, abs(n))
        return r if n > 0 else 1/r

    def pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        is_even = n % 2 == 0

        if is_even:
            return self.pow(x, int(n/2)) * self.pow(x, int(n/2))
        else:
            return x * self.pow(x, int(n/2)) * self.pow(x, int(n/2))


tests = [
    ([float(2), 10], 1024),
    ([float(2.1), 3], 9.26100),
    ([float(2), -2], 1/4)
]


for A, r in tests:
    round_digit = len(''.join(str(r).split('.')[1:]))
    a = round(Solution().myPow(A[0], A[1]), round_digit)

    if a != r:
        print(f"\033[91m -> {a} # {r}")
    else:
        print(f"\033[92m -> OK")
