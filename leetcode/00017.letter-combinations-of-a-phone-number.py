from typing import List
import time


mapping = {
    '2': list('abc'),
    '3': list('def'),
    '4': list('ghi'),
    '5': list('jkl'),
    '6': list('mno'),
    '7': list('pqrs'),
    '8': list('tuv'),
    '9': list('wxyz'),
}


class Solution:
    # (n^2) & log2(n)
    def getDict(self, num):
        if num:
            return mapping[num] if num in mapping.keys() else []
        return mapping

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        if len(digits) == 1:
            return self.getDict(digits[0])

        pivot = round(len(digits)/2)
        left = self.letterCombinations(digits[:pivot])
        right = self.letterCombinations(digits[pivot:])

        sets = []
        for l in left:
            for r in right:
                sets.append(l+r)

        return sets


tests = [
    ('23', ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ('293847568191281233412312', ["ad", "ae",
                                  "af", "bd", "be", "bf", "cd", "ce", "cf"]),
]

for A,  r in tests:
    start_time = time.time()
    a = Solution().letterCombinations(A)
    exec_time = (time.time() - start_time)
    if a != r or exec_time > 1:
        print(f"\033[91m -> {a} # {r} | {exec_time}")
    else:
        print(f"\033[92m -> OK | {exec_time}")
