from typing import List

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        pair_sum_set = set()
        nums.sort()
        left, right = 0, len(nums) - 1

        while left < right:
            curr_sum = nums[left] + nums[right]
            pair_sum_set.add(curr_sum)
            left, right = left + 1, right - 1
        
        return len(pair_sum_set)