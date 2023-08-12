from typing import List

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        left = right = ans = 0
        while right < len(nums):
            while right < len(nums) and nums[right] == nums[left]:
                right += 1
                if right == len(nums):
                    return ans
            left, right, ans = left + 1, right + 1, ans + 1
        return ans