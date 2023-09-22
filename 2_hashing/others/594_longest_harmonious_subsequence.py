from collections import Counter

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        ct = Counter(nums)
        return max(ct[k] + ct[k + 1] if k + 1 in ct else 0 for k in ct)