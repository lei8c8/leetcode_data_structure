from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}

        for i, v in enumerate(nums):
            if target - v in idx_map:
                return [idx_map[target - v], i]
            idx_map[v] = i
        