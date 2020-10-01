import math


class Solution:
    def intToRoman(self, num: int) -> str:
        r, numDigits = '', int(math.log10(num)) + 1
        hash_values = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
        }

        for i in range(int(numDigits)):
            place = round(pow(10, (numDigits - i - 1)))
            firstNum = int(num/place)

            if firstNum == 4:
                r += hash_values[place]
                r += hash_values[place * 5]

            elif firstNum == 9:
                r += hash_values[place]
                r += hash_values[place * 10]

            else:
                if firstNum > 4:
                    r += hash_values[place * 5]
                for i in range(firstNum % 5):
                    r += hash_values[place]
            num -= firstNum*place
        return r


tests = [
    (1994, 'MCMXCIV'),
]

for A,  r in tests:
    a = Solution().intToRoman(A)
    if a != r:
        print(f"\033[91m{A} -> {a} # {r}")
    else:
        print(f"\033[92m{A} -> OK")
