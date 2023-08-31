class Solution:
    def waysToSplitArray(self, nums):
        total = sum(nums)
        ans, left_sum = 0, 0
    
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum = total - left_sum
            if left_sum >= right_sum:
                ans += 1
        
        return ans
        