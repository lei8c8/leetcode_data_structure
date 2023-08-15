class Solution:
    def twoSumLessThanK(self, nums, k):
        nums.sort()
        left, right = 0, len(nums) - 1
        ans = -1
        while left < right:
            total = nums[left] + nums[right]
            if total < k:
                ans = max(ans, total)
                left += 1
            else:
                right -= 1
        return ans
