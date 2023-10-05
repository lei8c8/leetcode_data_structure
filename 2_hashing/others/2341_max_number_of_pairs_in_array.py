from typing import List
from collections import Counter

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ct = Counter(nums)
        pairs = sum(v // 2 for v in ct.values())
        return [pairs, len(nums) - 2 * pairs]