from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count, left, right = 0, 0, len(nums) - 1

        while left < right:
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] < nums[right]:
                nums[left + 1] += nums[left]
                left += 1
                count += 1
            else:
                nums[right - 1] += nums[right]
                right -= 1
                count += 1

        return count 