class Solution:
    def minimumDifference(self, nums, k):
        nums.sort()
        ans, left = float('inf'), 0
        for right in range(k - 1, len(nums)):
            diff = nums[right] - nums[left]
            ans = min(ans, diff)
            left += 1
        return ans 
        
       
        