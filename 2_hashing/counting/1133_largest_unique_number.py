from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums):
        ct = Counter(nums)
        ans = -1
        for key in ct:
            if ct[key] == 1:
                ans = max(ans, key)
        return ans