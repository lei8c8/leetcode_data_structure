from collections import Counter

class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        ct = Counter(nums)
        ans = 0

        for key in ct:
            if key - k in ct:
                ans += ct[key - k] * ct[key]

        return ans