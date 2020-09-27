class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x

        mi, ma, r, s = -(2 ** 31), (2 ** 31)-1, '', ''
        if x < 0:
            r = '-'
            s = str(x)[1:]
        else:
            s = str(x)

        l = len(s)
        for i in range(l):
            r += s[-i-1]
        return int(r) if mi <= int(r) <= ma else 0

# Other solution - use math
# class Solution:
#     def reverse(self, x: int) -> int:
#         rev = 0
#         # Fix error when we operated in negative number
#         p = 1
#         if x < 0:
#             x = -x
#             p = -p

#         INT_MAX = (2 ** 31)-1
#         INT_MIN = -(2 ** 31)

#         while x != 0:
#             pop = x % 10
#             x = (x - pop)/10
#             if (rev > INT_MAX/10 or (rev == INT_MAX / 10 and pop > 7)):
#                 return 0
#             if (rev < INT_MIN/10 or (rev == INT_MIN / 10 and pop < -8)):
#                 return 0
#             rev = rev * 10 + pop

#         return int(rev*p)


tests = [
    (123, 321),
    (120, 21),
    (-123, -321),
]


for t,  r in tests:
    a = Solution().reverse(t)
    if a != r:
        print(f"{a} # {r}")
