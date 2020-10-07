class Solution:
    # KMP algorithm
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if not haystack or len(haystack) < len(needle):
            return -1

        f = -1

        h, n, prefixLength = 0, 0, self.getPrefixLength(needle)
        while h < len(haystack):
            _n = needle[n]
            _h = haystack[h]
            if needle[n] == haystack[h]:
                h += 1
                n += 1

                if n == len(needle):
                    return h-n
            else:
                n = prefixLength[n]
                if n < 0:
                    h += 1
                    n += 1

        return f

    def getPrefixLength(self, needle: str) -> [str]:
        hash_prefix, i, prefix_length = [0]*(len(needle)+1), 1, 0
        hash_prefix[0] = -1
        hash_prefix[1] = 0
        while i < len(needle):
            if needle[prefix_length] == needle[i]:
                prefix_length += 1
                i += 1
                hash_prefix[i] = prefix_length
            elif prefix_length > 0:
                prefix_length = hash_prefix[prefix_length]
            else:
                i += 1
                hash_prefix[i] = 0
        return hash_prefix


tests = [
    (['hello', 'll'], 2),
    (['aaaaa', 'baa'], -1),
    (['a', 'a'], 0),
    (["mississippi", "issip"], 4),
    (["mississippi", "issipi"], -1),
    (["oqiabcxxxabcuajfacabcxxxabcyoinc", "abcxxxabcy"], 18)
]

for A,  r in tests:
    a = Solution().strStr(A[0], A[1])
    if a != r:
        print(f"\033[91m -> {a} # {r}")
    else:
        print(f"\033[92m -> OK")
