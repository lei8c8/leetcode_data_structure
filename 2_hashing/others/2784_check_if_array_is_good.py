from collections import Counter

class Solution:
    def isGood(self, nums: list[int]) -> bool:
        n = max(nums)
        ct = Counter(nums)

        for num in range(1, n + 1):
            if num < n:
                if ct[num] != 1:
                    return False
            elif num == n:
                if ct[num] != 2:
                    return False
        return True