from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, n = 0, len(nums) - 1, len(nums)
        ans = [0] * n

        i = right
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                ans[i] = nums[left] * nums[left]
                left += 1
            else:
                ans[i] = nums[right] * nums[right]
                right -= 1
            i -= 1

        return ans