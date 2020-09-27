class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        length = len(s)
        max_length, left, right = 0, 0, 0

        while left < length and right < length:
            if s[right] not in chars:
                chars.add(s[right])
                right += 1
                max_length = max(max_length, right-left)
            else:
                chars.remove(s[right])
                left += 1

        return max_length


# https://www.youtube.com/watch?time_continue=405&v=wiGpQwVHdE0&feature=emb_title
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         chars = set()
#         max_length, left = 0, 0

#         for right in range(len(s)):
#             while s[right] in chars:
#                 chars.remove(s[left])
#                 left += 1
#             chars.add(s[right])
#             max_length = max(max_length, right-left+1)
#         return max_length
