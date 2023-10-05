from collections import Counter

class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        ct = Counter(nums1 + nums2)
        num = 10

        for key in ct:
            if ct[key] == 2:
                num = min(num, key)

        if num != 10:
            return num

        x, y = min(nums1), min(nums2)
        return min(x, y) * 10 + max(x, y)


        