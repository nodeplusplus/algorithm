from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not len(nums1) and not len(nums2):
            return 0

        t = []

        l = len(nums1) + len(nums2)
        m = l/2
        i = 0
        j = 0

        while True:
            if (i+j) > m:
                break
            _t = t[-1] if len(t) else 0
            _n1 = 0
            _n2 = 0

            if i < len(nums1) and j < len(nums2):
                if nums1[i] - _t < nums2[j] - _t:
                    t.append(nums1[i])
                    i += 1
                else:
                    t.append(nums2[j])
                    j += 1
            elif i < len(nums1):
                t.append(nums1[i])
                i += 1
            elif j < len(nums2):
                t.append(nums2[j])
                j += 1

        if l % 2 == 0:
            return (t[-1] + t[-2]) / 2

        return t[-1]

# Algorithm: Binary search
# ---
# Other solution here
# https://www.youtube.com/watch?v=LPFhl65R7ww
# Better explanation
# https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46
