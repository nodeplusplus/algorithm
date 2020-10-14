INT_MIN, INT_MAX = -(2 ** 31), (2 ** 31)-1


# # Stupid
# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         count, result = 0, abs(dividend)
#         positive = (dividend > 0 and divisor > 0) or (
#             dividend < 0 and divisor < 0)

#         while result > abs(divisor):
#             result -= divisor
#             count += 1
#             if count >= INT_MAX:
#                 return INT_MAX

#         return count if positive else -count


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        i, j = 0, 0
        x, y = 0, 0
        dividend, divisor = abs(dividend), abs(divisor)

        remain = dividend - (y+x)
        while remain >= divisor:
            x += x if x > 0 else divisor
            i += i if i > 0 else 1

            if y+x+x > dividend:
                y += x
                j += i
                i, x = 0, 0

            if y+x > dividend:
                break

            remain = dividend - (y+x)

        res = j if flag else -j
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX

        return res


tests = [
    ([1, 1], 1),
    # ([10, 3], 3),
    # ([22, 3], 7),
    # ([100, 3], 33),
    # ([1, 3], 0),
    # ([-100, 3], -33),
    # ([INT_MAX, 2], int(INT_MAX / 2)),
]

for A,  r in tests:
    a = Solution().divide(A[0], A[1])
    if a != r:
        print(f"\033[91m {A[0]}/{A[1]} -> {a} # {r}")
    else:
        print(f"\033[92m {A[0]}/{A[1]} -> OK")
