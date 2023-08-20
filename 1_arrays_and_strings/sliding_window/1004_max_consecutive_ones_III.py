class Solution:
    def longestOnes(self, nums, k):
        left = ans = curr_ones = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr_ones += 1
            while curr_ones > k:
                if nums[left] == 0:
                    curr_ones -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans