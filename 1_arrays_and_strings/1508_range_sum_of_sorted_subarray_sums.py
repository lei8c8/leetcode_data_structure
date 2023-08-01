from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        all_sums = []
        for i in range(len(nums)):
            value = 0
            for j in range(i, len(nums)):
                value += nums[j]
                all_sums.append(value)
        
        all_sums.sort()
        return sum(all_sums[left - 1:right]) % 1000000007