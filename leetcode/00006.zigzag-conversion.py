class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        if l <= 2 or l <= numRows or numRows == 1:
            return s

        t, col_space = [], 2*(numRows-1)
        for i in range(numRows):
            _t, j = '', 0

            # Top and bottom
            if i == 0 or i == numRows-1:
                while i+col_space*j < l:
                    _t += s[i+col_space*j]
                    j += 1
                t.append(_t)
            # Between
            else:
                row_space = 2*(numRows-i-1)
                while i+col_space*j < l:
                    _t += s[i+col_space*j]
                    if i+col_space*j+row_space < l:
                        _t += s[i+col_space*j+row_space]
                    j += 1
                t.append(_t)

        return ''.join(t)

# Better solution
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1:
#             return s

#         rows = {k: '' for k in range(numRows)}
#         curRow = 0
#         goingDown = False

#         for c in s:
#             rows[curRow] += c
#             if curRow == 0 or curRow == numRows-1:
#                 goingDown = not goingDown
#             curRow += 1 if goingDown else -1

#         return ''.join(list(rows.values()))


tests = [
    ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
    ('PAYPALISHIRING', 4, 'PINALSIGYAHRPI'),
    ('PAYPALISHIRING', 5, 'PHASIYIRPLIGAN'),
    ('AB', 1, 'AB'),
    ('ABC', 1, 'ABC'),
]


for t, n, r in tests:
    a = Solution().convert(t, n)
    if a != r:
        print(f"{a} # {r}")

# P   A   H   N
# A P L S I I G
# Y   I   R

# 4|0   4   8     12
# 2|1 3 5 7 9  11 13
# 0|2   6   10

# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# 6| 0     6      12
# 4| 1   5 7   11 13
# 2| 2 4   8 10
# 0| 3     9

# P     H
# A   S I
# Y  I  R
# P L   I G
# A     N


# 8| 0     8
# 6| 1   7 9
# 4| 2  6  10
# 2| 3 5   11 13
# 0| 4     12
